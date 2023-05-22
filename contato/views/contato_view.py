from django.shortcuts import render
from contato.models import Contato
# Create your views here.

def index(request):
    contatos = Contato.objects.all()
    
    context = {
        'contatos': contatos,
    }
    
    return render(request, 'contato/index.html', context)