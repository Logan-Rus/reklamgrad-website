# Импорт модуля models из django.db.
# Этот модуль предоставляет базовые классы для создания моделей Django.
# Модели представляют таблицы в базе данных и используются для работы с данными.
from django.db import models

class Work(models.Model):
    """
    Класс:
        - Work: для хранения информации о работе.

    Поля:
        - title2: Название работы (не больше 200 букв).
        - tip: Дополнительная информация о работе.
        - description2: Подробное описание работы.
        - image2: Изображение, связанное с работой.
    """
    title2 = models.CharField(max_length=200, verbose_name="")
    tip = models.TextField(verbose_name="", blank=True, null=True)
    description2 = models.TextField(verbose_name="", blank=True, null=True)
    image2 = models.ImageField(upload_to='works/', verbose_name="")

    def __str__(self):
        """
        Функция __str__:
                - self.title2: Возвращает название работы для отображения.
        """
        return self.title2


class Service(models.Model):
    """
        Класс:
            - Service: для хранения информации об услуге.

        Поля:
            - title: Название услуги (не больше 200 букв).
            - description: Подробное описание услуги.
            - image: Изображение, связанное с услугой.
        """
    title = models.CharField(max_length=200, verbose_name="")
    description = models.TextField(verbose_name="", blank=True, null=True)
    image = models.ImageField(upload_to='services/', verbose_name="")

    def __str__(self):
        """
        Функция __str__:
                - self.title: Возвращает название услуги для отображения.
        """
        return self.title

