# Импорт необходимых модулей и классов Django для тестирования
from django.test import TestCase

# Импорт моделей, которые будут тестироваться
from .models import Service, Work

# Импорт функций для работы с URL-адресами
from django.urls import resolve, reverse

# Импорт представлений (views), которые будут тестироваться
from .views import home, all_services, service_detail, all_works, work_detail


class ModelTests(TestCase):
    """
    Класс для тестирования моделей приложения.
    Проверяет, что модели корректно создаются и сохраняют данные.
    """

    def test_create_service(self):
        """
        Тест для проверки создания модели `Service`.
        Проверяет, что:
        1. Объект `Service` корректно создается.
        2. Поля `title` и `description` содержат ожидаемые значения.
        """
        # Создаем тестовый объект услуги
        service = Service.objects.create(
            title="Тестовая услуга",
            description="Описание тестовой услуги",
            image="services/test.jpg"
        )

        # Проверяем, что поле `title` содержит ожидаемое значение
        self.assertEqual(service.title, "Тестовая услуга")

        # Проверяем, что поле `description` содержит ожидаемое значение
        self.assertEqual(service.description, "Описание тестовой услуги")

    def test_create_work(self):
        """
        Тест для проверки создания модели `Work`.
        Проверяет, что:
        1. Объект `Work` корректно создается.
        2. Поля `title2`, `description2` и `tip` содержат ожидаемые значения.
        """
        # Создаем тестовый объект работы
        work = Work.objects.create(
            title2="Тестовая работа",
            description2="Описание тестовой работы",
            image2="works/test.jpg",
            tip="Тип работы"
        )

        # Проверяем, что поле `title2` содержит ожидаемое значение
        self.assertEqual(work.title2, "Тестовая работа")

        # Проверяем, что поле `description2` содержит ожидаемое значение
        self.assertEqual(work.description2, "Описание тестовой работы")

        # Проверяем, что поле `tip` содержит ожидаемое значение
        self.assertEqual(work.tip, "Тип работы")


class URLTests(TestCase):
    """
    Класс для тестирования URL-адресов приложения.
    Проверяет, что URL-адреса корректно сопоставляются с соответствующими представлениями (views).
    """

    def test_home_url(self):
        """
        Тест для проверки URL главной страницы (home).
        Проверяет, что URL 'home' корректно сопоставляется с представлением `home`.
        """
        # Получаем URL по имени маршрута
        url = reverse('home')

        # Проверяем, что URL сопоставляется с правильным представлением
        self.assertEqual(resolve(url).func, home)

    def test_all_services_url(self):
        """
        Тест для проверки URL страницы со всеми услугами (all_services).
        Проверяет, что URL 'all_services' корректно сопоставляется с представлением `all_services`.
        """
        # Получаем URL по имени маршрута
        url = reverse('all_services')

        # Проверяем, что URL сопоставляется с правильным представлением
        self.assertEqual(resolve(url).func, all_services)

    def test_service_detail_url(self):
        """
        Тест для проверки URL страницы деталей услуги (service_detail).
        Проверяет, что URL 'service_detail' корректно сопоставляется с представлением `service_detail`.
        """
        # Создаем тестовый объект услуги в базе данных
        service = Service.objects.create(
            title="Тестовая услуга",
            description="Описание тестовой услуги",
            image="services/test.jpg"
        )

        # Получаем URL по имени маршрута и передаем аргумент (id услуги)
        url = reverse('service_detail', args=[service.id])

        # Проверяем, что URL сопоставляется с правильным представлением
        self.assertEqual(resolve(url).func, service_detail)

    def test_all_works_url(self):
        """
        Тест для проверки URL страницы со всеми работами (all_works).
        Проверяет, что URL 'all_works' корректно сопоставляется с представлением `all_works`.
        """
        # Получаем URL по имени маршрута
        url = reverse('all_works')

        # Проверяем, что URL сопоставляется с правильным представлением
        self.assertEqual(resolve(url).func, all_works)

    def test_work_detail_url(self):
        """
        Тест для проверки URL страницы деталей работы (work_detail).
        Проверяет, что URL 'work_detail' корректно сопоставляется с представлением `work_detail`.
        """
        # Создаем тестовый объект работы в базе данных
        work = Work.objects.create(
            title2="Тестовая работа",
            description2="Описание тестовой работы",
            image2="works/test.jpg",
            tip="Тип работы"
        )

        # Получаем URL по имени маршрута и передаем аргумент (id работы)
        url = reverse('work_detail', args=[work.id])

        # Проверяем, что URL сопоставляется с правильным представлением
        self.assertEqual(resolve(url).func, work_detail)


class TemplateTests(TestCase):
    """
    Класс для тестирования шаблонов (HTML-страниц) приложения.
    Наследуется от django.test.TestCase для использования функционала тестирования Django.
    """

    def test_home_template(self):
        """
        Тест для проверки главной страницы (home).
        Проверяет, что:
        1. Страница возвращает статус 200 (успешный запрос).
        2. На странице присутствует текст "REKLAMGRAD".
        3. На странице присутствует текст "Ваша реклама — наше искусство!".
        """
        # Получаем ответ от сервера при запросе главной страницы
        response = self.client.get(reverse('home'))

        # Проверяем, что ответ содержит текст "REKLAMGRAD"
        self.assertContains(response, "REKLAMGRAD")

        # Проверяем, что ответ содержит текст "Ваша реклама — наше искусство!"
        self.assertContains(response, "Ваша реклама — наше искусство!")

    def test_service_detail_template(self):
        """
        Тест для проверки страницы деталей услуги (service_detail).
        Проверяет, что:
        1. Страница возвращает статус 200 (успешный запрос).
        2. На странице присутствует название услуги.
        3. На странице присутствует описание услуги.
        """
        # Создаем тестовый объект услуги в базе данных
        service = Service.objects.create(
            title="Тестовая услуга",
            description="Описание тестовой услуги",
            image="services/test.jpg"
        )

        # Получаем ответ от сервера при запросе страницы деталей услуги
        response = self.client.get(reverse('service_detail', args=[service.id]))

        # Проверяем, что ответ содержит название услуги
        self.assertContains(response, "Тестовая услуга")

        # Проверяем, что ответ содержит описание услуги
        self.assertContains(response, "Описание тестовой услуги")

    def test_work_detail_template(self):
        """
        Тест для проверки страницы деталей работы (work_detail).
        Проверяет, что:
        1. Страница возвращает статус 200 (успешный запрос).
        2. На странице присутствует название работы.
        3. На странице присутствует описание работы.
        """
        # Создаем тестовый объект работы в базе данных
        work = Work.objects.create(
            title2="Тестовая работа",
            description2="Описание тестовой работы",
            image2="works/test.jpg",
            tip="Тип работы"
        )

        # Получаем ответ от сервера при запросе страницы деталей работы
        response = self.client.get(reverse('work_detail', args=[work.id]))

        # Проверяем, что ответ содержит название работы
        self.assertContains(response, "Тестовая работа")

        # Проверяем, что ответ содержит описание работы
        self.assertContains(response, "Описание тестовой работы")