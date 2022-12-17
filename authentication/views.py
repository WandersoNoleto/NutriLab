from django.http import HttpResponse
from django.shortcuts import render


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":
         username = request.POST.get('usuario')
         password = request.POST.get('senha')
         confirm_password = request.POST.get('confirmar_senha')
         email    = request.POST.get('email')
         

         return HttpResponse(confirm_password)

def login(request):
    return HttpResponse("Voce está na pagina de login")
