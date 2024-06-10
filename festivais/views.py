from django.shortcuts import render
from .models import *

def festival_view (request):
    context = {
        'festivais' : Festival.objects.all(),
        'bandas' : Banda.objects.all(),
        }


    return render(request, 'festivais/festival.html', context)

def banda_view(request,festival_id):
    context = {
        'festival' : Festival.objects.get(id = festival_id)
        }

    return render(request, 'festivais/detalhes.html', context)