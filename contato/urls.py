from django.urls import path
from .views import index

app_name = 'contato'

urlpatterns = [
    path('', index, name="index")
]
