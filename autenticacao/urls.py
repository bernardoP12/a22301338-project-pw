from django.urls import path
from . import views

app_name = 'autenticacao'

urlpatterns = [
    path('logout/', views.logout_view, name="sair"),
    path('login/', views.login_view, name="entrar"),

    path('register/', views.register_view, name="registar"),

]