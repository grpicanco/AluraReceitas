from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from receitas.models import Receita


# Create your views here.

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if not nome.split():
            messages.error(request, 'Nome deve ser preenchido')
            return redirect('cadastro')
        if not email.split():
            messages.error(request, 'Email error')
            return redirect('cadastro')
        if password != password2:
            messages.error(request, 'As senhas devem ser iguais')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário ja cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=password)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso')
        return redirect('login')
    print('nao foi metodo post')
    return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['senha']

        if not email or not password:
            messages.error(request, 'Preencha todos os campos')
            return redirect('login')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso')
                return redirect('dashboard')
        else:
            messages.error(request, 'Login Invalido')
            return redirect('login')
    return render(request, 'usuarios/login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso')
    return redirect('index')


def dashboard(request):
    if request.user.is_authenticated:
        receitas = Receita.objects.filter(pessoa=request.user.id).order_by('-criado_em')

        dados = {
            'receitas': receitas
        }
        return render(request, 'usuarios/dashboard.html', dados)
    return redirect('index')


def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        img = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)

        receita = Receita.objects.create(nome_receita=nome_receita, rendimento=rendimento, ingredientes=ingredientes,
                                         modo_preparo=modo_preparo, tempo_preparo=tempo_preparo, categoria=categoria,
                                         pessoa=user, img=img)

        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_receitas.html')
