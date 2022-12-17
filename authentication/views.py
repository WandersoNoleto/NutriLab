import os

from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.shortcuts import get_object_or_404, redirect, render

from .models import ActiveUser
from .utils import email_html, password_is_valid


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":
         username = request.POST.get('usuario')
         password = request.POST.get('senha')
         confirm_password = request.POST.get('confirmar_senha')
         email    = request.POST.get('email')

         if not password_is_valid(request, password, confirm_password):
            return redirect('/auth/cadastro')
         
         try:
            user = User.objects.create_user(username=username,
																		email=email,
                                    password=password,
                                    is_active=False)
            user.save()

            path_template = os.path.join(settings.BASE_DIR, 'autenticacao/templates/emails/confirm_register.html')
            email_html(path_template, 'Cadastro confirmado', [email,], username=username, link_ativacao="127.0.0.1:8000/auth/ativar_conta/{token}")
            messages.add_message(request, constants.ERROR, 'Usuario cadastrado com sucesso')
            return redirect('/auth/login')
         
         except:
            messages.add_message(request, constants.ERROR, 'Error')
            return redirect('/auth/cadastro')

def login(request):
    if request.method == "GET":
      if request.user.is_authenticated:
            return redirect('/')
      return render(request, 'login.html')

    elif request.method == "POST":
         username = request.POST.get('usuario')
         password = request.POST.get('senha')

         user = auth.authenticate(username=username, password=password)

         if not user:
            messages.add_message(request, constants.ERROR, 'Uusário ou senha inválidos')
            return redirect('/auth/login')
         else:
            auth.login(request, user)
            return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/auth/login')

def active_account(request, token):
    token = get_object_or_404(ActiveUser, token=token)
    if token.ativo:
        messages.add_message(request, constants.WARNING, 'Essa token já foi usado')
        return redirect('/auth/login')
    user = User.objects.get(username=token.user.username)
    user.is_active = True
    user.save()
    token.active = True
    token.save()
    messages.add_message(request, constants.SUCCESS, 'Conta ativa com sucesso')
    return redirect('/auth/login')



