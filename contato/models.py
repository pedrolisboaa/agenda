from django.db import models
from django.utils import timezone

# Create your models here.


class Contato(models.Model):
    primeiro_nome = models.CharField(name='Nome', max_length=100)
    segundo_nome = models.CharField(name='Sobrenome', max_length=150)
    telefone = models.CharField(name='Telefone', max_length=11)
    email = models.EmailField(name='Email', max_length=256, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(name='Descrição', blank=True)

    def __str__(self):
        return self.primeiro_nome