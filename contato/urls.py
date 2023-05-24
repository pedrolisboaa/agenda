from django.urls import path
from .views import index, contato, buscar, criacao

app_name = 'contato'

urlpatterns = [
    path('', index, name="index"),
    path('buscar/', buscar, name="buscar"),

    # Contato (CRUD)
    path('contato/<int:contato_id>/detalhe/', contato, name="contato"),
    path('contato/criacao/', criacao, name="criacao"),
    #path('contato/<int:contato_id>/atualizacao/', contato, name="contato"),
    #path('contato/<int:contato_id>/apagando/', contato, name="contato"),
    
]
