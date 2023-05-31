from django.urls import path
from .views import index, contato, buscar, criacao, atualizacao, deletar, registro, login_view, logout_view

app_name = 'contato'

urlpatterns = [
    path('', index, name="index"),
    path('buscar/', buscar, name="buscar"),

    # Contato (CRUD)
    path('contato/<int:contato_id>/detalhe/', contato, name="contato"),
    path('contato/criacao/', criacao, name="criacao"),
    path('contato/<int:contato_id>/atualizacao/', atualizacao, name="atualizacao"),
    path('contato/<int:contato_id>/deletar/', deletar, name="deletar"),

    # usuario

    path('usuario/registro/', registro, name='registro'),
    path('usuario/login/', login_view, name='login'),
    path('usuario/logout/', logout_view, name='logout'),
    
]
