from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    """
    Класс, представляющий пользователя веб-сайта для нагрузочного тестирования.
    Наследуется от HttpUser, предоставляемого библиотекой Locust.
    """

    # Время ожидания между задачами (от 1 до 5 секунд)
    wait_time = between(1, 5)

    def __init__(self, *args, **kwargs):
        """
        Инициализация пользователя.
        Устанавливает тайм-ауты для подключения и запросов.
        """
        super().__init__(*args, **kwargs)
        self.client.connection_timeout = 10  # Тайм-аут подключения (в секундах)
        self.client.request_timeout = 10  # Тайм-аут выполнения запроса (в секундах)

    @task
    def load_main_page(self):
        """
        Задача: Загрузка главной страницы.
        Метод отправляет GET-запрос на корневой URL ("/").
        """
        self.client.get("/")

    @task(3)
    def load_services_page(self):
        """
        Задача: Загрузка страницы услуг.
        Метод отправляет GET-запрос на URL "/services/".
        Вес задачи: 3 (выполняется в 3 раза чаще, чем задачи с весом 1).
        """
        self.client.get("/services/")

    @task(2)
    def load_works_page(self):
        """
        Задача: Загрузка страницы работ.
        Метод отправляет GET-запрос на URL "/works/".
        Вес задачи: 2 (выполняется в 2 раза чаще, чем задачи с весом 1).
        """
        self.client.get("/works/")

    @task
    def load_about_page(self):
        """
        Задача: Загрузка страницы "О нас".
        Метод отправляет GET-запрос на URL "/about".
        """
        self.client.get("/about")

    @task
    def load_contact_page(self):
        """
        Задача: Загрузка страницы контактов.
        Метод отправляет GET-запрос на URL "/contact".
        """
        self.client.get("/contact")