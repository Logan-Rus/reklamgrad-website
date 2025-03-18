from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client.connection_timeout = 10  # Тайм-аут подключения
        self.client.request_timeout = 10  # Тайм-аут запроса

    @task
    def load_main_page(self):
        self.client.get("/")

    @task(3)
    def load_services_page(self):
        self.client.get("/services/")

    @task(2)
    def load_works_page(self):
        self.client.get("/works/")

    @task
    def load_about_page(self):
        self.client.get("/about")  # Переход на страницу "О нас"

    @task
    def load_contact_page(self):
        self.client.get("/contact")  # Переход на страницу контактов