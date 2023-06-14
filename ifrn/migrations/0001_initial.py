# Generated by Django 4.2.2 on 2023-06-14 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Curso",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=200)),
                ("descricao", models.CharField(max_length=200)),
                ("imagem", models.ImageField(upload_to="imagens")),
                ("data", models.DateField()),
            ],
        ),
    ]