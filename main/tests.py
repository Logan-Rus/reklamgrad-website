from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from .models import (
    StaticPage, Work, Service, Advantage,
    MainPage, MenuItem, ContactRequest, Footer
)


class StaticPageModelTest(TestCase):
    """Тестирование модели StaticPage"""

    def test_static_page_creation(self):
        """
        Тест создания статической страницы.
        Проверяет:
        - Корректное сохранение заголовка и slug
        - Автоматическое заполнение дат создания/обновления
        - Строковое представление объекта
        """
        page = StaticPage.objects.create(
            title="О компании",
            slug="about",
            content="<p>О нашей компании</p>",
            meta_title="О компании | Наш сайт"
        )
        self.assertEqual(page.title, "О компании")
        self.assertEqual(page.slug, "about")
        self.assertTrue(page.created_at <= timezone.now())
        self.assertEqual(str(page), "О компании")

    def test_slug_uniqueness(self):
        """
        Тест уникальности slug.
        Проверяет, что невозможно создать две страницы с одинаковым slug.
        """
        StaticPage.objects.create(title="Page 1", slug="page")
        with self.assertRaises(Exception):
            StaticPage.objects.create(title="Page 2", slug="page")


class WorkModelTest(TestCase):
    """Тестирование модели Work"""

    def setUp(self):
        self.image = SimpleUploadedFile(
            "work.jpg",
            b"file_content",
            content_type="image/jpeg"
        )

    def test_work_creation(self):
        """
        Тест создания работы.
        Проверяет:
        - Сохранение заголовка и описания
        - Загрузку изображения в правильную директорию
        - Необязательное поле tip
        - Строковое представление
        """
        work = Work.objects.create(
            title="Логотип компании",
            description="Создание логотипа",
            tip="Графика",
            image=self.image
        )
        self.assertEqual(work.title, "Логотип компании")
        self.assertEqual(work.tip, "Графика")
        self.assertTrue(work.image.name.startswith('works/'))
        self.assertEqual(str(work), "Логотип компании")


class ServiceModelTest(TestCase):
    """Тестирование модели Service"""

    def setUp(self):
        """Создание тестового изображения для услуги"""
        self.image = SimpleUploadedFile(
            "service.jpg",
            b"file_content",
            content_type="image/jpeg"
        )

    def test_service_creation(self):
        """
        Тест создания услуги.
        Проверяет:
        - Корректное сохранение данных
        - Загрузку изображения
        - Строковое представление
        """
        service = Service.objects.create(
            title="Веб-дизайн",
            description="Создание дизайна сайтов",
            image=self.image
        )
        self.assertEqual(service.title, "Веб-дизайн")
        self.assertTrue(service.image.name.startswith('services/'))
        self.assertEqual(str(service), "Веб-дизайн")


class AdvantageModelTest(TestCase):
    """Тестирование модели Advantage"""

    def setUp(self):
        """Создание главной страницы для связи"""
        self.main_page = MainPage.objects.create(
            title="Главная страница",
            description="Описание главной страницы"
        )

    def test_advantage_creation(self):
        """
        Тест создания преимущества.
        Проверяет:
        - Связь с главной страницей
        - Порядок сортировки
        - Строковое представление
        """
        advantage = Advantage.objects.create(
            main_page=self.main_page,
            title="Опыт 10 лет",
            description="Мы работаем с 2013 года",
            order=1
        )
        self.assertEqual(advantage.title, "Опыт 10 лет")
        self.assertEqual(advantage.main_page, self.main_page)
        self.assertEqual(advantage.order, 1)
        self.assertEqual(str(advantage), "Опыт 10 лет")


class MainPageModelTest(TestCase):
    """Тестирование модели MainPage"""

    def setUp(self):
        """Создание тестового фонового изображения"""
        self.image = SimpleUploadedFile(
            "bg.jpg",
            b"file_content",
            content_type="image/jpeg"
        )

    def test_main_page_creation(self):
        """
        Тест создания главной страницы.
        Проверяет:
        - Сохранение всех основных полей
        - Загрузку фонового изображения
        - Строковое представление
        """
        main_page = MainPage.objects.create(
            title="Рекламное агентство",
            description="Лучшие рекламные решения",
            image=self.image,
            title_about="О нас",
            description_about="Наша история",
            title_service="Наши услуги",
            title_work="Наши работы"
        )
        self.assertEqual(main_page.title, "Рекламное агентство")
        self.assertTrue(main_page.image.name.startswith('homepage/'))
        self.assertEqual(str(main_page), "Рекламное агентство")


class MenuItemModelTest(TestCase):
    """Тестирование модели MenuItem"""

    def test_menu_item_creation(self):
        """
        Тест создания пункта меню.
        Проверяет:
        - Сохранение заголовка и URL
        - Порядок сортировки
        - Строковое представление
        """
        item = MenuItem.objects.create(
            title="Главная",
            url="/",
            order=1
        )
        self.assertEqual(item.title, "Главная")
        self.assertEqual(item.order, 1)
        self.assertEqual(str(item), "Главная")

    def test_default_ordering(self):
        """
        Тест порядка сортировки пунктов меню.
        Проверяет, что пункты сортируются по полю order.
        """
        MenuItem.objects.create(title="Услуги", url="/services/", order=2)
        MenuItem.objects.create(title="Главная", url="/", order=1)
        items = MenuItem.objects.all()
        self.assertEqual(items[0].title, "Главная")
        self.assertEqual(items[1].title, "Услуги")


class ContactRequestModelTest(TestCase):
    """Тестирование модели ContactRequest"""

    def test_contact_request_creation(self):
        """
        Тест создания контактной заявки.
        Проверяет:
        - Сохранение email и сообщения
        - Автоматическую дату создания
        - Формат строкового представления
        """
        request = ContactRequest.objects.create(
            email="test@example.com",
            message="Нужна консультация"
        )
        self.assertEqual(request.email, "test@example.com")
        self.assertTrue(request.created_at <= timezone.now())
        self.assertIn("test@example.com", str(request))

    def test_ordering(self):
        """
        Тест сортировки заявок.
        Проверяет, что заявки сортируются по убыванию даты создания.
        """
        old = ContactRequest.objects.create(
            email="old@test.com",
            message="Старая заявка"
        )
        old.created_at = timezone.now() - timezone.timedelta(days=1)
        old.save()

        new = ContactRequest.objects.create(
            email="new@test.com",
            message="Новая заявка"
        )

        requests = ContactRequest.objects.all()
        self.assertEqual(requests[0].email, "new@test.com")


class FooterModelTest(TestCase):
    """Тестирование модели Footer"""

    def test_footer_creation(self):
        """
        Тест создания настроек футера.
        Проверяет:
        - Сохранение основных полей
        - Строковое представление
        """
        footer = Footer.objects.create(
            company_title="РекламГрад",
            contact_phone="+79991234567",
            contact_email="info@reklamgrad.ru",
            copyright_text="© 2023 РекламГрад"
        )
        self.assertEqual(footer.company_title, "РекламГрад")
        self.assertEqual(footer.contact_phone, "+79991234567")
        self.assertEqual(str(footer), "Настройки футера")

    def test_load_method(self):
        """
        Тест метода load() (singleton-паттерн).
        Проверяет, что метод всегда возвращает один и тот же экземпляр.
        """
        # Первый вызов создает объект
        footer1 = Footer.load()
        # Второй вызов получает существующий
        footer2 = Footer.load()
        self.assertEqual(footer1.pk, footer2.pk)