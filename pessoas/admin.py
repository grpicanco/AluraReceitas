from django.contrib import admin
from .models import Pessoa


# Register your models here.
class PessoaLista(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'dt_nascimento')
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_per_page = 5


admin.site.register(Pessoa, PessoaLista)
