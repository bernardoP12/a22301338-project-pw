from django.urls import path
from . import views


app_name = "meteo"

urlpatterns = [
    path('api/cidades/', views.api_lista_cidades, name='api_lista_cidades'),
    path('api/previsao/hoje/<int:city_id>/', views.api_previsao_hoje, name='api_previsao_hoje'),
    path('api/previsao/cinco_dias/<int:city_id>/', views.previsao_cinco_dias, name='api_previsao_cinco_dias'),
    path('tempo/hoje/lisboa/', views.tempo_hoje_lisboa, name='tempo_hoje_lisboa'),
    path('cidades/', views.cidades, name='cidades'),
    path('previsao/<int:city_id>/', views.previsao_cinco_dias, name='previsao_cinco_dias'),
    path('tempo/<int:city_id>/', views.tempo_hoje_cidade, name='tempo_hoje_cidade'),
]
