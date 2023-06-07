from django.shortcuts import render, redirect
from contato.forms import RegistroForm, AtualizacaoRegistro
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def registro(request):
    form = RegistroForm()

    if request.method == 'POST':
        form = RegistroForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request,'Usuário registrado com sucesso!')
            return redirect('contato:index')
    


    context = {
        'form': form
    }
    
    return render(request, 'contato/registro.html', context)


def login_view(request):
    form = AuthenticationForm(request, data=request.POST)

    if request.method == 'POST':
        if form.is_valid():
            usuario = form.get_user()
            messages.success(request, 'Logado com sucesso.')
            auth.login(request, usuario)
            return redirect('contato:index')
        
    messages.error(request, 'Login inválido.')


    return render(request,'contato/login.html', {'form': form})


def logout_view(request):
    auth.logout(request)
    return redirect('contato:login')


def atualizar_usuario(request):
    form = AtualizacaoRegistro(instance=request.user)
    if request.method != 'POST':
        return render(request,'contato/registro.html', {'form': form})
    

    form = AtualizacaoRegistro(data=request.POST, instance=request.user)
    if not form.is_valid():
        return render(request,'contato/registro.html', {'form': form})
    
    form.save()
    return render(request,'contato/registro.html', {'form': form})
