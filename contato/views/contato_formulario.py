from django.shortcuts import render, get_object_or_404, redirect
from contato.models import Contato

def criacao(request):
    return render(request, 'contato/criacao.html' )