# Импорт модуля models из django.db.
# Этот модуль предоставляет базовые классы для создания моделей Django.
# Модели представляют таблицы в базе данных и используются для работы с данными.
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils import timezone

class StaticPage(models.Model):
    """
    Класс:
        - StaticPage: для статических страниц сайта.
    """
    meta_title = CKEditor5Field(max_length=250, blank=True, verbose_name="Мета-заголовок")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL")
    title = CKEditor5Field(max_length=250, verbose_name="Заголовок")
    content = CKEditor5Field(verbose_name="Содержание")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статическая страница"
        verbose_name_plural = "Статические страницы"

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
    title = CKEditor5Field(max_length=200, verbose_name="Название работы")
    tip = CKEditor5Field(verbose_name="Тип работы", blank=True, null=True)
    description = CKEditor5Field(verbose_name="Описание", blank=True, default="")
    image = models.ImageField(upload_to='works/', verbose_name="Изображение")

    class Meta:
        verbose_name = "Данные об разделе Портфолио"
        verbose_name_plural = "Данные об разделе Портфолио"

    def __str__(self):
        """
        Функция __str__:
                - self.title2: Возвращает название работы для отображения.
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

    class Meta:
        verbose_name = "Данные об разделе Услуги"
        verbose_name_plural = "Данные об разделе Услуги"

    def __str__(self):
        """
        Функция __str__:
                - self.title: Возвращает название услуги для отображения.
        """
        return self.title


class Advantage(models.Model):
    """
    Класс для хранения преимуществ компании
    Связана с MainPage через ForeignKey
    """
    main_page = models.ForeignKey(
        'MainPage',
        on_delete=models.CASCADE,
        related_name='advantages',
        verbose_name="Главная страница"
    )
    title = CKEditor5Field(
        max_length=200,
        verbose_name="Заголовок преимущества"
    )
    description = CKEditor5Field(
        verbose_name="Описание преимущества"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Порядок сортировки"
    )

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"
        ordering = ['order']

    def __str__(self):
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

    title_about = CKEditor5Field(verbose_name="Заголовок раздела О нас")
    image_about = models.ImageField(upload_to='about/', verbose_name="Изображение")
    description_about = CKEditor5Field(verbose_name="Описание раздела ", null=True)

    title_service = CKEditor5Field(verbose_name="Заголовок раздела Сервисы")
    description_service = CKEditor5Field(verbose_name="Описание второго раздела", blank=True, null=True)

    title_work = CKEditor5Field(verbose_name="Заголовок раздела Работы")
    description_work = CKEditor5Field(verbose_name="Описание третьего раздела", blank=True, null=True)

    contact_title = CKEditor5Field(verbose_name="Заголовок формы обратной связи", blank=True, null=True)

    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = "Главная страница"

    def __str__(self):
        """
        Функция __str__:
                - self.title: Возвращает название услуги для отображения.
        """
        return self.title

class MenuItem(models.Model):
    """
    Класс для пунктов навигационного меню
    """
    title = models.CharField(max_length=100, verbose_name="Название")
    url = models.CharField(max_length=200, verbose_name="URL или якорь")
    order = models.PositiveIntegerField(default=0)  # Для сортировки

    class Meta:
        ordering = ['order']
        verbose_name = "Пункт навигационного меню"
        verbose_name_plural = "Пункты навигационного меню"

    def __str__(self):
        """Строковое представление объекта для удобного отображения в админке и shell."""
        return self.title


class ContactRequest(models.Model):
    """
    Класс для хранения контактных заявок от пользователей.
    
    Поля:
      - email (EmailField): Электронная почта отправителя.
      - message (TextField): Текст сообщения от пользователя.
      - created_at (DateTimeField): Дата и время создания заявки (автоматически устанавливается при создании).
    """
    
    email = models.EmailField(
        verbose_name="Email"
    )
    message = models.TextField(
        verbose_name="Сообщение"
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата отправки"
    )

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ['-created_at']  # Сортировка по убыванию даты (новые заявки сверху)

    def __str__(self):
        """Строковое представление объекта в формате: 'Заявка от email (дата)'."""
        return f"Заявка от {self.email} ({self.created_at.strftime('%d.%m.%Y %H:%M')})"


class Footer(models.Model):
    """
    Класс для хранения информации футера сайта
    """
    # Секция "О компании"
    company_title = CKEditor5Field(
        "Название компании",
        blank=True,
        null=True,
        default=''
    )
    company_description = CKEditor5Field(
        "Описание компании",
        blank=True,
        null=True
    )

    # Контактная информация
    contact_phone_title = CKEditor5Field(
        "Заголовок телефона",
        blank=True,
        null=True,
        default=''
    )
    contact_phone = models.CharField(
        "Телефон",
        max_length=20,
        default=""
    )
    contact_email_title = CKEditor5Field(
        "Заголовок email",
        blank=True,
        null=True,
        default=''
    )
    contact_email = models.EmailField(
        "Email",
        default=""
    )

    # Меню футера
    menu_nav_title = CKEditor5Field(
        "Заголовок меню навигации",
        blank=True,
        null=True,
        default=''
    )
    menu_services_title = CKEditor5Field(
        "Заголовок меню услуг",
        blank=True,
        null=True,
        default=''
    )
    menu_works_title = CKEditor5Field(
        "Заголовок меню работ",
        blank=True,
        null=True,
        default=''
    )

    # Социальные сети
    social_vk_url = models.URLField(
        "Ссылка VK",
        default="",
        blank=True
    )

    # Копирайт
    copyright_text = CKEditor5Field(
        "Текст копирайта",
        default=''
    )

    @classmethod
    def load(cls):
        """
        Загружает или создает единственный экземпляр настроек футера
        """
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    class Meta:
        verbose_name = "Футер"
        verbose_name_plural = "Футер"

    def __str__(self):
        return "Настройки футера"
