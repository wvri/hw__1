from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)  # Название статьи
    text = models.TextField()  # Текст статьи
    author = models.CharField(max_length=255)  # Автор статьи

    def __str__(self):
        return self.title  # Показывать название статьи в админке
     