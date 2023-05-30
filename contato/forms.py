from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contato



class ContatoForm(forms.ModelForm):

    imagem = forms.ImageField(
        widget=forms.FileInput(
            attrs = {
                'accept': 'imagem/*',
            }
        )
    )

    class Meta:
        model = Contato
        fields = ('primeiro_nome', 'segundo_nome', 'imagem', 'telefone', 'email', 'categoria', 'descricao')
 
        # widgets = {'primeiro_nome': forms.PasswordInput(attrs=
        # {'class': 'classe-a classe-b','placeholder': 'Infome seu nome', }), }

    def clean(self):
        cleaned_data = self.cleaned_data
        primeiro_nome = cleaned_data.get('primeiro_nome')
        segundo_nome = cleaned_data.get('segundo_nome')
        
        if primeiro_nome == segundo_nome:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )

            self.add_error('primeiro_nome', msg)
            self.add_error('segundo_nome', msg)
        return super().clean()

    def clean_first_name(self):
        primeiro_nome = self.cleaned_data.get('primeiro_nome')

        if primeiro_nome == 'ABC':
            self.add_error(
                'primeiro_nome',
                ValidationError(
                    'Veio do add_error',
                    code='invalid'
                )
            )

        return primeiro_nome


class RegistroForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2'
        )
    
    def clean_email(self):
        # Aqui é para não deixar terem e-mails iguais.
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Jé existe este e-mail', code='invalid')
            )

        return email