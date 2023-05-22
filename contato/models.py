from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    nome = models.CharField(max_length=125)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    primeiro_nome = models.CharField(max_length=100)
    segundo_nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=50)
    email = models.EmailField(max_length=256, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    visivel = models.BooleanField(default=True)
    imagem = models.ImageField(blank=True, upload_to='imagens/%Y/%m/')
    categoria = models.ForeignKey(Categoria,
                                  on_delete=models.SET_NULL,
                                  blank=True, null=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self):
        return self.primeiro_nome
