from django.urls import path
from .views import index, contato

app_name = 'contato'

urlpatterns = [
    path('', index, name="index"),
    path('<int:contato_id>/', contato, name="contato")
]
