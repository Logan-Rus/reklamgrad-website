from django.db import models

class Review(models.Model):
    author = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.author}'

class Collection(models.Model):
    title = models.CharField(max_length=100)  # Название коллекции
    base_characteristics = models.TextField(verbose_name="Основные характеристики", blank=True, null=True)
    metall = models.CharField(max_length=100, verbose_name="Металл", blank=True, null=True)
    vstavka = models.CharField(max_length=100, verbose_name="Вставка", blank=True, null=True)
    description = models.TextField(max_length=100, verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(upload_to='collections/')  # Поле для изображения

    def __str__(self):
        return self.title