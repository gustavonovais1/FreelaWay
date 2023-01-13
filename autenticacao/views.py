from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

def cadastro(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/jobs/encontrar_jobs')
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username =  request.POST.get('username')
        password = request.POST.get('password')
        confirmar_password = request.POST.get('confirm-password')
        if not password == confirmar_password:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/auth/cadastro')
        if len(username.strip()) == 0 or len(password.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/auth/cadastro')
        
        user = User.objects.filter(username=username)
        if user.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usário com esse username')
            return redirect('/auth/cadastro')

    try:
        user = User.objects.create_user(username=username,
        password=password)
        user.save()
        messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso')
        return redirect('/auth/login')
    except:
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
        return redirect('/auth/cadastro')

def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/encontrar_jobs')
        return render(request, 'logar.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        usuario = auth.authenticate(username=username, password=senha)
    if not usuario:
        messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
        return redirect('/auth/login')
    else:
        auth.login(request, usuario)
        return redirect('/jobs/encontrar_jobs')

def sair(request):
    auth.logout(request)
    return redirect('/auth/login')
