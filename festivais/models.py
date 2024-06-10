from django.db import models

class Banda (models.Model):
    nomeBanda = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.nomeBanda}'

class Localizacao (models.Model):
    cidade = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.cidade}'

class Festival (models.Model):
    nomeFestival = models.CharField(max_length=100)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    capa = models.ImageField(upload_to="capas",null = True, blank = True, default = None)
    def __str__(self):
        return f'{self.nomeFestival}'
