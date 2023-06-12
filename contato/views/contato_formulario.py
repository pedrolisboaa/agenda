from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from contato.forms import ContatoForm
from contato.models import Contato


app_name = 'contato'

@login_required(login_url='contato:login')
def criacao(request):
    form_action = reverse('contato:criacao')

    if request.method == 'POST':
        form = ContatoForm(request.POST, request.FILES )

        contexto = {
            'form': form,
            'form_action': form_action,
            }

        if form.is_valid():
            contato = form.save(commit=False)
            contato.owner = request.user
            contato.save()
            return redirect('contato:atualizacao', contato_id=contato.pk)

        return render(request, 'contato/criacao.html', contexto)
    
    contexto = {
        'form': ContatoForm(),
        'form_action': form_action,
    }

    return render(request, 'contato/criacao.html', contexto)


@login_required(login_url='contato:login')
def atualizacao(request, contato_id):
    contato = get_object_or_404(Contato, pk=contato_id, visivel=True, owner=request.user)
    form_action = reverse('contato:atualizacao', args=(contato_id,))

    if request.method == 'POST':
        form = ContatoForm(request.POST, request.FILES, instance=contato)

        contexto = {
            'form': form,
            'form_action': form_action,
            }

        if form.is_valid():
            contato = form.save()
            return redirect('contato:atualizacao', contato_id=contato.pk)

        return render(request, 'contato/criacao.html', contexto)
    
    contexto = {
        'form': ContatoForm(instance=contato),
        'form_action': form_action,
    }

    return render(request, 'contato/criacao.html', contexto)

@login_required(login_url='contato:login')
def deletar(request, contato_id):
    contato  = get_object_or_404(
        Contato, pk=contato_id, visivel=True,
        owner=request.user
    )

    confirmacao = request.POST.get('confirmacao', 'nao')
    if confirmacao == 'sim':
        contato.delete()
        return redirect('contato:index')

    print(confirmacao)

    # contato.delete()
    # return redirect('contato:index')

    return render(
        request,
        'contato/contato.html',
        {
            'contato':contato,
            'confirmacao': confirmacao,
        }
    )