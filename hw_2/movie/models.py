from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)  # Название фильма
    description = models.TextField()  # Описание фильма
    producer = models.CharField(max_length=255)  # Продюсер
    duration = models.IntegerField()  # Длительность (в секундах)

    def __str__(self):
        return self.title  # Показывать название фильма в админке
