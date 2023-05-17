from django.contrib import admin
from .models import Contato, Categoria

# Register your models here.


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'primeiro_nome',
        'segundo_nome',
        'email',
        #'data_criacao',
        'categoria',)
    ordering = '-id',
    search_fields = 'id', 'Nome'
    list_per_page = 30
    list_max_show_all = 400
    list_filter = 'categoria',
    list_display_links = 'id', 'primeiro_nome',
    
    
    @admin.register(Categoria)
    class CategoriaAdmin(admin.ModelAdmin):
        list_display = ('nome',)
