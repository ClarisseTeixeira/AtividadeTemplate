from django.contrib import admin
from .models import Curso
# Register your models here.

@admin.register(Curso)
class AdmimCurso(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'imagem')
