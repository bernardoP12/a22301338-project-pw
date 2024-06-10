from django.shortcuts import render
from .models import *

def curso_view(request):
    context = {
        'cursos' : Curso.objects.all(),
    }

    return render (request, 'cursos/index.html', context)

def disciplinas_view(request, disciplina_id):
    context = {

        'disciplinas' : Disciplina.objects.all(),
        'disciplina' : Disciplina.objects.get(id = disciplina_id),
        'ano1' : Disciplina.objects.filter(ano=1),
        'ano2' : Disciplina.objects.filter(ano=2),
        'ano3' : Disciplina.objects.filter(ano=3),
        'semestre1' : Disciplina.objects.filter(semestre ='1º Semestre'),
        'semestre2' : Disciplina.objects.filter(semestre ='2º Semestre'),
    }

    return render(request, 'cursos/disciplinas.html', context)


def disciplina_view(request, disciplina_id):
    context = {

        'disciplina' : Disciplina.objects.get(id = disciplina_id)
    }

    return render(request, 'cursos/disciplina.html', context)