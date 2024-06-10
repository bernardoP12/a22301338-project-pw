from django import forms
from .models import Banda, Album, Musica
from django.contrib.auth.models import User

class UserRegistrationFrom(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username','first_name','last_name','email','password']

    widgets = {'password':forms.PasswordInput}


class AlbumForm(forms.ModelForm):
  capa = forms.ImageField(required=False)
  class Meta:
    model = Album
    fields = '__all__'
    help_texts = {
            'banda': 'Nome da banda.',
            'titulo': 'Titulo do album.',
            'ano': 'Ano de lancamento.',
            'capa': 'Fotografia da capa do album.',
        }

class BandaForm(forms.ModelForm):
    foto = forms.ImageField(required=False)
    class Meta:
        model = Banda
        fields = '__all__'

        help_texts = {
            'nome': 'Nome da banda.',
            'nacionalidade': 'Nacionalidade da banda.',
            'genero': 'Genero musical da banda.',
            'ano': 'Ano de criacao da banda.',
            'foto': 'Fotografia da banda.',
        }

class MusicaForm(forms.ModelForm):
  class Meta:
    model = Musica
    fields = '__all__'
    help_texts = {
            'album': 'Nome do album.',
            'titulo': 'Titulo da música.',
            'duracao': 'Duracao.',
            'spotify_link': 'Link do spotify.',
            'letra': 'Letra da música.',
            'biografia': 'Biografia (4-5 linhas).',
        }

