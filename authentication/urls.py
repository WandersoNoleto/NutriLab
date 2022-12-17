from django.urls import path

from . import views

urlpatterns = [
    path('cadastro/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('sair/', views.logout, name="logout"),
    path('ativar_conta/<str:token>/', views.active_account, name="active_account")
]
