from django.shortcuts import render, get_object_or_404, redirect
from contato.models import Contato
from contato.forms import ContatoForm

app_name = 'contato'


def criacao(request):

    if request.method == 'POST':
        contexto = {
            'form': ContatoForm(request.POST)
        }

        return render(request, 'contato/criacao.html', contexto)
   
    contexto = {
        'form': ContatoForm()
    }

    return render(request, 'contato/criacao.html', contexto)
