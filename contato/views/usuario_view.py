from django.shortcuts import render
from contato.forms import RegistroForm
from django.contrib import messages

def registro(request):
    form = RegistroForm()

    

    if request.method == 'POST':
        form = RegistroForm(request.POST)
        
        if form.is_valid():
            form.save()


    context = {
        'form': form
    }
    
    return render(request, 'contato/registro.html', context)