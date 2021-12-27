from django.shortcuts import render, get_object_or_404
from .models import Receita


# Create your views here.

def index(request):
    receitas = Receita.objects.filter(ativo=True).order_by('-criado_em')

    dados = {
        'receitas': receitas
    }
    return render(request, 'index.html', dados)


def receita(request, id):
    receita = get_object_or_404(Receita, pk=id)
    dados = {
        'receita': receita
    }
    return render(request, 'receita.html', dados)


def buscar(request):
    lista_receitas = Receita.objects.filter(ativo=True).order_by('-criado_em')

    if request.GET['buscar']:
        nome_a_buscar = request.GET['buscar']
        lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'buscar.html', dados)
