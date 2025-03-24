# Импорт модуля models из django.db.
# Этот модуль предоставляет базовые классы для создания моделей Django.
# Модели представляют таблицы в базе данных и используются для работы с данными.
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class PageWork(models.Model):
    """
        Класс:
            - PageWork: для хранения контента страницы с работами.

        Поля:
            - title: Основной заголовок страницы
            - description: Описание раздела страницы
            - footer_*: Элементы подвала страницы
            - more_work: Заголовок блока дополнительных работ
        """
    title = CKEditor5Field(verbose_name="Заголовок раздела")
    description = CKEditor5Field(verbose_name="Описание раздела", blank=True, null=True)

    footer_titleCompany = CKEditor5Field(verbose_name="Название компании", blank=True, null=True)
    footer_descriptionCompany = CKEditor5Field(verbose_name="Описание компании", blank=True, null=True)
    footer_titleNumber = CKEditor5Field(verbose_name="Заголовок отображение контактной информации 1", blank=True, null=True)
    footer_titleEmail = CKEditor5Field(verbose_name="Заголовок отображение контактной информации 2", blank=True, null=True)
    footer_titleMenu = CKEditor5Field(verbose_name="Название первого раздела в футере", blank=True, null=True)
    footer_titleMenu2 = CKEditor5Field(verbose_name="Название второго раздела в футере", blank=True, null=True)
    footer_titleMenu3 = CKEditor5Field(verbose_name="Название третьего раздела в футере", blank=True, null=True)

    more_work = CKEditor5Field(verbose_name="Заголовок новых работ", blank=True, null=True, default="")

    def __str__(self):
        """
        Функция __str__:
                - self.title: Возвращает название услуги для отображения.
        """
        return self.title

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
    title2 = CKEditor5Field(max_length=200, verbose_name="Название работы")
    tip = CKEditor5Field(verbose_name="Тип работы", blank=True, null=True)
    description2 = CKEditor5Field(verbose_name="Описание", blank=True, default="")
    image2 = models.ImageField(upload_to='works/', verbose_name="Изображение")

    def __str__(self):
        """
        Функция __str__:
                - self.title2: Возвращает название работы для отображения.
        """
        return self.title2

class PageService(models.Model):
    """
       Класс:
            -PageService: для хранения контента страницы с услугами.

       Включает:
       - Основные заголовки и описания
       - Контактную информацию
       - Элементы футера
       - Дополнительные разделы
    """
    title = CKEditor5Field(verbose_name="Заголовок раздела")
    description = CKEditor5Field(verbose_name="Описание раздела", blank=True, null=True)

    contact_title = CKEditor5Field(verbose_name="Заголовок формы обратной связи", blank=True, null=True)

    footer_titleCompany = CKEditor5Field(verbose_name="Название компании", blank=True, null=True)
    footer_descriptionCompany = CKEditor5Field(verbose_name="Описание компании", blank=True, null=True)
    footer_titleNumber = CKEditor5Field(verbose_name="Заголовок отображение контактной информации 1", blank=True, null=True)
    footer_titleEmail = CKEditor5Field(verbose_name="Заголовок отображение контактной информации 2", blank=True, null=True)
    footer_titleMenu = CKEditor5Field(verbose_name="Название первого раздела в футере", blank=True, null=True)
    footer_titleMenu2 = CKEditor5Field(verbose_name="Название второго раздела в футере", blank=True, null=True)
    footer_titleMenu3 = CKEditor5Field(verbose_name="Название третьего раздела в футере", blank=True, null=True)

    right_titleMenu = CKEditor5Field(verbose_name="Название раздела справа", blank=True, null=True)

    def __str__(self):
        """
        Функция __str__:
                - self.title: Возвращает название услуги для отображения.
        """
        return self.title

class Service(models.Model):
    """
        Класс:
            - Service: для хранения информации об услуге.

        Поля:
            - title: Название услуги (не больше 200 букв).
            - description: Подробное описание услуги.
            - image: Изображение, связанное с услугой.
        """

    title = CKEditor5Field(max_length=200, verbose_name="Название услуги")
    description = CKEditor5Field(verbose_name="Описание", blank=True, default="")
    image = models.ImageField(upload_to='services/', verbose_name="Изображение")

    def __str__(self):
        """
        Функция __str__:
                - self.title: Возвращает название услуги для отображения.
        """
        return self.title

class MainPage(models.Model):
    """
        Класс:
            - MainPage: главная страница сайта.

        Содержит все контентные блоки главной страницы:
        - Hero-секция (заголовок, описание, фон)
        - О компании
        - Преимущества (3 блока)
        - Услуги
        - Работы
        - Контакты
        - Футер
    """

    title = CKEditor5Field(verbose_name="Заголовок главной страницы")
    description = CKEditor5Field(verbose_name="Описание главной страницы", blank=True, default="")
    image = models.ImageField(upload_to='homepage/', verbose_name="Background-изображение главной страницы")

    title_about = CKEditor5Field(verbose_name="Заголовок первого раздела")
    image_about = models.ImageField(upload_to='about/', verbose_name="Изображение")
    description_about = CKEditor5Field(verbose_name="Описание первого раздела", blank=True, null=True)
    # Поля для преимуществ
    advantage1_title = CKEditor5Field(verbose_name="Заголовок преимущества 1")
    advantage1_description = CKEditor5Field(verbose_name="Описание преимущества 1")
    advantage2_title = CKEditor5Field(verbose_name="Заголовок преимущества 2")
    advantage2_description = CKEditor5Field(verbose_name="Описание преимущества 2")
    advantage3_title = CKEditor5Field(verbose_name="Заголовок преимущества 3")
    advantage3_description = CKEditor5Field(verbose_name="Описание преимущества 3")

    title_service = CKEditor5Field(verbose_name="Заголовок второго раздела")
    description_service = CKEditor5Field(verbose_name="Описание второго раздела", blank=True, null=True)

    title_work = CKEditor5Field(verbose_name="Заголовок третьего раздела")
    description_work = CKEditor5Field(verbose_name="Описание третьего раздела", blank=True, null=True)

    contact_title = CKEditor5Field(verbose_name="Заголовок формы обратной связи", blank=True, null=True)
    contact_text = CKEditor5Field(verbose_name="Текст формы обратной связи", blank=True, null=True)

    footer_titleCompany = CKEditor5Field(verbose_name="Название компании", blank=True, null=True)
    footer_descriptionCompany = CKEditor5Field(verbose_name="Описание компании", blank=True, null=True)
    footer_titleNumber = CKEditor5Field(verbose_name="Заголовок отображение контактной информации 1", blank=True, null=True)
    footer_titleEmail = CKEditor5Field(verbose_name="Заголовок отображение контактной информации 2", blank=True, null=True)
    footer_titleMenu = CKEditor5Field(verbose_name="Название первого раздела в футере", blank=True, null=True)
    footer_titleMenu2 = CKEditor5Field(verbose_name="Название второго раздела в футере", blank=True, null=True)
    footer_titleMenu3 = CKEditor5Field(verbose_name="Название третьего раздела в футере", blank=True, null=True)

    def __str__(self):
        """
        Функция __str__:
                - self.title: Возвращает название услуги для отображения.
        """
        return self.title
