# pwsite/views.py

from django.shortcuts import render

def index_view(request):
    return render(request, "pwsite/index.html")
    
def index_view2(request):
    return render(request, "pwsite/sobre.html")