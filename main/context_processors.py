# main/context_processors.py
# Импорт необходимых моделей из текущего приложения
from .models import MainPage, Service, Work, MenuItem, Footer

def common_context(request):
    """
        Контекстный процессор, добавляющий общие данные на все страницы сайта.

        Возвращает словарь с данными, которые будут доступны во всех шаблонах:
        - main_page: данные главной страницы (первый объект MainPage)
        - services: список всех услуг (QuerySet объектов Service)
        - latest_works: список всех работ, отсортированных по ID (QuerySet объектов Work)
        - menu_items: пункты меню, отсортированные по полю order
        - footer: данные футера (загружаются через метод load() модели Footer)

        Использование:
        1. Добавить в settings.TEMPLATES.OPTIONS.context_processors
        2. Данные будут автоматически доступны во всех шаблонах
    """
    return {
        'main_page': MainPage.objects.first(),
        'services': Service.objects.all(),
        'latest_works': Work.objects.all().order_by('id'),
        'menu_items': MenuItem.objects.all().order_by('order'),
        'footer': Footer.load(),
    }