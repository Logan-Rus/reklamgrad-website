# main/context_processors.py
# Импорт необходимых моделей из текущего приложения
import json
from .models import MainPage, Service, Work, MenuItem, Footer, StaticPage

from django.urls import resolve
from django.shortcuts import get_object_or_404


def common_context(request):
    """
    Контекстный процессор, добавляющий общие данные во все шаблоны.

    Возвращает словарь с часто используемыми данными сайта, чтобы
    не дублировать запросы в каждом представлении:
        - main_page: первый объект MainPage с данными главной страницы
        - services: все услуги (Service.objects.all())
        - latest_works: все работы (Work.objects.all()), отсортированные по ID
        - menu_items: пункты меню, отсортированные по полю order
        - footer: данные футера, загружаемые через кастомный метод Footer.load()

    Для использования:
    - Добавьте 'main.context_processors.common_context' в settings.py
      в TEMPLATES -> OPTIONS -> context_processors
    - Данные станут доступны во всех шаблонах
    """
    return {
        'main_page': MainPage.objects.first(),
        'services': Service.objects.all(),
        'latest_works': Work.objects.all().order_by('id'),
        'menu_items': MenuItem.objects.all().order_by('order'),
        'footer': Footer.load(),
    }

def jsonld_data(request):
    """
       Контекстный процессор для генерации JSON-LD разметки (структурированных данных)
       для SEO и улучшения представления в поисковых системах.

       Логика:
       - Определяется текущее имя URL (view) через resolve(request.path_info)
       - В зависимости от текущей страницы создается словарь с JSON-LD согласно
         спецификации schema.org и типу страницы
       - Для главной страницы — WebPage с общей информацией
       - Для статической страницы — WebPage с заголовком и описанием
       - Для страницы услуги — тип Service с названием, описанием и изображением
       - Для страницы работы — тип CreativeWork с данными работы
       - Можно добавить обработку других видов страниц при необходимости

       Возвращает словарь с ключом 'jsonld_data', в котором лежит JSON-строка.
       Если данные отсутствуют — возвращается пустой JSON-объект '{}'.

       В шаблонах использовать с фильтром safe, чтобы корректно вывести JSON.
    """
    current_view = resolve(request.path_info).url_name
    jsonld = None

    if current_view == 'home':
        # Для главной страницы
        try:
            main_page = MainPage.objects.first()
        except MainPage.DoesNotExist:
            main_page = None
        if main_page:
            jsonld = {
                "@context": "https://schema.org",
                "@type": "WebPage",
                "name": main_page.title or "Главная страница",
                "description": main_page.description[:160] if main_page.description else "",
                "url": request.build_absolute_uri(),
                "image": request.build_absolute_uri(main_page.image.url) if main_page.image else None,
            }

    elif current_view == 'static_page':
        # Разметка для статической страницы
        slug = resolve(request.path_info).kwargs.get('slug')
        if slug:
            page = get_object_or_404(StaticPage, slug=slug)
            jsonld = {
                "@context": "https://schema.org",
                "@type": "WebPage",
                "name": page.meta_title or page.title,
                "description": page.meta_description[:160] if page.meta_description else "",
                "url": request.build_absolute_uri(),
            }

    elif current_view == 'service_detail':
        # Разметка для страницы услуги
        object_id = resolve(request.path_info).kwargs.get('object_id')
        if object_id:
            service = get_object_or_404(Service, id=object_id)
            jsonld = {
                "@context": "https://schema.org",
                "@type": "Service",
                "name": service.title,
                "description": service.description[:160] if service.description else "",
                "image": request.build_absolute_uri(service.image.url) if service.image else None,
                "url": request.build_absolute_uri(),
            }

    elif current_view == 'work_detail':
        # Разметка для страницы портфолио
        object_id = resolve(request.path_info).kwargs.get('object_id')
        if object_id:
            work = get_object_or_404(Work, id=object_id)
            jsonld = {
                "@context": "https://schema.org",
                "@type": "CreativeWork",
                "name": work.title,
                "description": work.description[:160] if work.description else "",
                "image": request.build_absolute_uri(work.image.url) if work.image else None,
                "url": request.build_absolute_uri(),
            }

    return {'jsonld_data': json.dumps(jsonld) if jsonld else '{}'}
