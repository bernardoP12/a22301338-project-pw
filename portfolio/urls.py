from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('about_me/', views.about_me, name='about_me'),
    path('about_website/', views.about_website, name='about_website'),
]