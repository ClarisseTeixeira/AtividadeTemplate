from django.shortcuts import render
from .models import Curso
from django.shortcuts import get_object_or_404
# Create your views here.

def lista_curso(request):
    curso = Curso.objects.all()
    context = {'lista_curso': curso}
    return render(request, "index.html", context)

def pag_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    context = {'pag_curso': curso}
    return render(request, "curso.html", context)
    