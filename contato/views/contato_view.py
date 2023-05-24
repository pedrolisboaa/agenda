from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from contato.models import Contato
from django.db.models import Q
# Create your views here.

def index(request):
    contatos = Contato.objects.all().filter(visivel=True).order_by('-id')

    paginator = Paginator(contatos, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'site_titulo': 'Contatos '
    }
    
    return render(request, 'contato/index.html', context)


def buscar(request):
    valor_de_busca = request.GET.get('q', '').strip()

    if valor_de_busca == '':
        return redirect('contato:index')

    # filtando nome pela parada de busca
    # Se utiliar vírgua é "E" como Q e o | eu crio um "ou"
    contatos = Contato.objects \
    .filter(visivel=True) \
    .filter(
        Q(primeiro_nome__icontains=valor_de_busca) | 
        Q(segundo_nome__icontains=valor_de_busca) |
        Q(telefone__icontains=valor_de_busca) |
        Q(email__icontains=valor_de_busca)
    ).order_by('-id')

    paginator = Paginator(contatos, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_titulo': 'Contatos '
    }
    
    return render(request, 'contato/index.html', context)



def contato(request, contato_id):
    #contato = Contato.objects.get(pk=contato_id)
    contato = get_object_or_404(Contato, pk=contato_id, visivel=True)
    
    context = {
        'contato': contato,
        'site_titulo': f'{contato.primeiro_nome} {contato.segundo_nome}'
    }
    
    return render(request, 'contato/contato.html', context)

