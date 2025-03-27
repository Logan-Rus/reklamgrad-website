# Импорт модуля models из django.db.
# Этот модуль предоставляет базовые классы для создания моделей Django.
# Модели представляют таблицы в базе данных и используются для работы с данными.
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

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

    class Meta:
        verbose_name = "Данные об разделе Работы"
        verbose_name_plural = "Данные об разделе Работы"

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
    description_about = CKEditor5Field(verbose_name="Описание раздела ", blank=True, null=True)

    # Поля для преимуществ
    advantage1_title = CKEditor5Field(verbose_name="Заголовок преимущества 1")
    advantage1_description = CKEditor5Field(verbose_name="Описание преимущества 1")
    advantage2_title = CKEditor5Field(verbose_name="Заголовок преимущества 2")
    advantage2_description = CKEditor5Field(verbose_name="Описание преимущества 2")
    advantage3_title = CKEditor5Field(verbose_name="Заголовок преимущества 3")
    advantage3_description = CKEditor5Field(verbose_name="Описание преимущества 3")

    title_service = CKEditor5Field(verbose_name="Заголовок раздела Сервисы")
    description_service = CKEditor5Field(verbose_name="Описание второго раздела", blank=True, null=True)

    title_work = CKEditor5Field(verbose_name="Заголовок раздела Работы")
    description_work = CKEditor5Field(verbose_name="Описание третьего раздела", blank=True, null=True)

    contact_title = CKEditor5Field(verbose_name="Заголовок формы обратной связи", blank=True, null=True)
    contact_text = CKEditor5Field(verbose_name="Текст формы обратной связи", blank=True, null=True)

    # Футер - информация о компании
    footer_titleCompany = CKEditor5Field("Название компании", blank=True, null=True)
    footer_descriptionCompany = CKEditor5Field("Описание компании", blank=True, null=True)
    footer_titleNumber = CKEditor5Field("Заголовок телефона", blank=True, null=True)
    footer_phone = models.CharField("Телефон", max_length=20, default="+7 (915) 777-73-14")
    footer_titleEmail = CKEditor5Field("Заголовок email", blank=True, null=True)
    footer_email = models.EmailField("Email", default="reklamgrad@mail.ru")

    # Футер - меню
    footer_titleMenu = CKEditor5Field("Заголовок меню навигации", blank=True, null=True)
    footer_titleMenu2 = CKEditor5Field("Заголовок меню услуг", blank=True, null=True)
    footer_titleMenu3 = CKEditor5Field("Заголовок меню работ", blank=True, null=True)

    # Социальные сети
    footer_vk_url = models.URLField("Ссылка VK", default="https://vk.com/reklamgrad")

    # Копирайт
    footer_copyright = CKEditor5Field("Текст копирайта", default='&copy; 2025&nbsp; <a class="footer_btn" href="http://127.0.0.1:8000/#">REKLAMGRAD</a>')

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
    Класс для хранения пунктов навигационного меню.
    
    Поля:
        - main_page (ForeignKey): Связь с главной страницей, к которой относится пункт меню. При удалении главной страницы все связанные пункты меню удаляются (CASCADE).
        - title (CharField): Название пункта меню (максимальная длина - 100 символов).
        - url (CharField): URL-адрес или якорная ссылка для пункта меню (максимальная длина - 200 символов).
    """
    
    main_page = models.ForeignKey(
        'MainPage', 
        on_delete=models.CASCADE, 
        related_name='menu_items',
        verbose_name="Главная страница"
    )
    title = models.CharField(
        max_length=100, 
        verbose_name="Название пункта навигационного меню"
    )
    url = models.CharField(
        max_length=200, 
        verbose_name="URL или якорь"
    )

    class Meta:
        verbose_name = "Пункт навигационного меню"
        verbose_name_plural = "Пункты навигационного меню"
        # По умолчанию Django будет использовать ordering = ['id']

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
