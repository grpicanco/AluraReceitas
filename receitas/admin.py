from django.contrib import admin
from .models import Receita


# Register your models here.

class ReceitaLista(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'ativo')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_editable = ('ativo',)
    list_per_page = 5


admin.site.register(Receita, ReceitaLista)
