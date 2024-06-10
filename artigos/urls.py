from django.urls import path
from . import views  # Importamos views para poder usar as suas funções

app_name = 'artigos'

urlpatterns = [

    path('artigos/<int:article_id>/', views.article_detail_view, name='article-detail'),
    path('comentarios/<int:comment_id>/', views.comment_detail_view, name='comment-detail'),
    path('avaliacoes/<int:rating_id>/', views.rating_detail_view, name='rating-detail'),
    path('artigos/', views.articles_list_view, name='index'),
    path('autores/', views.authors_list_view, name='author-list'),
    path('authors/<int:author_id>/', views.author_detail_view, name='author-detail'),


 ]


