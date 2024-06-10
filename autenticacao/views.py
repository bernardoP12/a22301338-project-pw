from django.shortcuts import render, redirect
from django.contrib.auth import  login, logout, models, authenticate

def logout_view(request):
    logout(request)
    return redirect('autenticacao:entrar')




def register_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('autenticacao:entrar')

    return render(request, 'autenticacao/registar.html')






def login_view(request):
    if request.method == 'POST':
        user = authenticate(
        request,
        username = request.POST['username'],
        password = request.POST['password'])

        login(request, user)
        return render(request, 'autenticacao/utilizador.html')


    return render(request,'autenticacao/entrar.html')