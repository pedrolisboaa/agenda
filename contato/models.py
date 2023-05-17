from django.db import models
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=125)
    
    def __str__(self):
        return self.nome


class Contato(models.Model):
    primeiro_nome = models.CharField(max_length=100)
    segundo_nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=256, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    visivel = models.BooleanField(default=True)
    imagem = models.ImageField(blank=True, upload_to='imagens/%Y/%m/')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.primeiro_nome
    