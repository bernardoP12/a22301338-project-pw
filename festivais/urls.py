from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'festivais'

urlpatterns = [
    path('festivais/', views.festival_view, name = 'festival'),
    path('detalhes/<int:festival_id>/', views.banda_view, name = 'detalhes'),
]