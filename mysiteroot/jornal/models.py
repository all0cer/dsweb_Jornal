from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Edicao(models.Model):
    data_edicao = models.DateField()
    titulo_edicao = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo_edicao

class Noticia(models.Model):
    edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=60)
    texto_noticia = models.TextField(max_length=255)
    data_noticia = models.DateField(default=timezone.now)

class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, null=True, blank=True)
    texto_comentario = models.CharField(max_length=255)


class Usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, null=True)
    email = models.EmailField()
    senha = models.CharField(max_length=60)

