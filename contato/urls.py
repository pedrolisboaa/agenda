from django.urls import path
from .views import index, contato, buscar

app_name = 'contato'

urlpatterns = [
    path('', index, name="index"),
    path('buscar/', buscar, name="buscar"),

    # Contato (CRUD)
    path('contato/<int:contato_id>/detail/', contato, name="contato"),
    
]
