from typing import Any, Dict
from django import forms
from django.core.exceptions import ValidationError
from .models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = 'primeiro_nome', 'segundo_nome', 'telefone', 'email', 'descricao', 'imagem', 'categoria',

    def clean(self):

        cleaned_data = self.cleaned_data

        self.add_error(
            'primeiro_nome',
            ValidationError(
                'Mensagem de erro',
                code='Invalido'
            )
        )

        return super().clean()