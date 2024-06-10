from django.urls import path
from . import views

app_name = 'bandas'

urlpatterns = [
    path('index/', views.index_view, name = 'index'),
    path('banda/<int:banda_id>/',views.banda_view, name = 'banda'),
    path('album/<int:album_id>/',views.album_view, name = 'album'),
    path('musica/<int:musica_id>/',views.musica_view, name = 'musica'),
    path('apaga_banda/<int:banda_id>/', views.apaga_banda_view, name="apagarBanda"),
    path('edita_album/<int:album_id>/', views.edita_album_view, name="editarAlbum"),
    path('apaga_album/<int:album_id>/', views.apaga_album_view, name="apagarAlbum"),
    path('edita_musica/<int:musica_id>/', views.edita_musica_view, name="editarMusica"),
    path('nova_banda', views.nova_banda_view, name="novaBanda"),
    path('novo_album/<int:banda_id>/', views.novo_album_view, name="novoAlbum"),
    path('nova_musica/<int:album_id>/', views.nova_musica_view, name="novaMusica"),
    path('edita_banda/<int:banda_id>/', views.edita_banda_view, name="editarBanda"),
    path('apaga_musica/<int:musica_id>/', views.apaga_musica_view, name="apagarMusica"),
]