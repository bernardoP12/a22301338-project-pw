from django.shortcuts import render

def index(request):
    return render(request, 'portfolio/index.html')

def about_me(request):
    return render(request, 'portfolio/about_me.html')

def about_website(request):
    return render(request, 'portfolio/about_website.html')