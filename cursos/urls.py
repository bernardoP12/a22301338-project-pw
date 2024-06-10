from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'cursos'

urlpatterns = [
    path('index/', views.curso_view, name = 'index'),
    path('disciplinas/<int:disciplina_id>/', views.disciplinas_view, name = 'disciplinas'),
    path('disciplina/<int:disciplina_id>/', views.disciplina_view, name = 'disciplina'),
]