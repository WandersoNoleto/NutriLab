from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .utils import password_is_valid


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
            messages.add_message(request, constants.ERROR, 'Usuario cadastrado com sucesso')
            return redirect('/auth/login')
         
         except Exception as error:
            messages.add_message(request, constants.ERROR, '[ERROR]:' + error)
            return redirect('/auth/cadastro')

def login(request):
    return HttpResponse("Voce está na pagina de login")
