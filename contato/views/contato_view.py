from django.shortcuts import render, get_object_or_404
from contato.models import Contato
# Create your views here.

def index(request):
    contatos = Contato.objects.all().filter(visivel=True).order_by('-id')
    
    context = {
        'contatos': contatos,
    }
    
    return render(request, 'contato/index.html', context)


def contato(request, contato_id):
    #contato = Contato.objects.get(pk=contato_id)
    contato = get_object_or_404(Contato, pk=contato_id, visivel=True)
    
    context = {
        'contato': contato,
    }
    
    return render(request, 'contato/contato.html', context)