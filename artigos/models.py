from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField()

    def str(self):
        return self.user.username

class Article(models.Model):
    title = models.CharField(max_length=200)
    corpo = models.TextField()
    data_Postada = models.DateTimeField(auto_now_add=True)
    ultima_modificacao = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)

    def str(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'comentario de {self.author.username} acerca {self.article.title}'


class Rating(models.Model):
    article = models.ForeignKey(Article, related_name='ratings', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField()

    def str(self):
        return f'Rating {self.score} for {self.article.title}'