from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import StaticPage, Work, Service

class StaticPageSitemap(Sitemap):
    """
       Sitemap для статических страниц сайта, например, страниц с произвольным содержимым.

       Атрибуты:
           changefreq (str): Рекомендуемая частота обновления страницы (monthly).
           priority (float): Приоритет страницы в карте сайта.
    """
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        """
        Возвращает QuerySet всех статических страниц.
        """
        return StaticPage.objects.all()

    def lastmod(self, obj):
        """
        Возвращает дату последнего обновления объекта для указания поисковым системам.
        """
        return obj.updated_at

    def location(self, obj):
        """
        Возвращает URL-адрес страницы на основе ее slug.
        """
        return f'/{obj.slug}/'

class WorkSitemap(Sitemap):
    """
        Sitemap для раздела с портфолио / работами.

        Атрибуты:
            changefreq (str): Рекомендуемая частота обновления страницы (monthly).
            priority (float): Приоритет страницы.
    """
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        """
        Возвращает все объекты Work.
        """
        return Work.objects.all()

    def lastmod(self, obj):
        """
        Не указывается дата изменения.
        """
        return None

    def location(self, obj):
        """
        Формирует URL для работы по ID.
        """
        return f'/work/{obj.id}/'

class ServiceSitemap(Sitemap):
    """
       Sitemap для страниц с услугами.

       Атрибуты:
           changefreq (str): Частота обновления (monthly).
           priority (float): Приоритет страницы.
    """
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        """
        Возвращает все объекты Service.
        """
        return Service.objects.all()

    def lastmod(self, obj):
        """
        Дата изменения не указывается.
        """
        return None

    def location(self, obj):
        """
        Формирует URL страницы услуги по ID.
        """
        return f'/service/{obj.id}/'

class StaticViewSitemap(Sitemap):
    """
        Sitemap для статичных представлений, таких как главная, контактная и прочие страницы,
        которые не связаны с моделями, а имеют именованные маршруты.

        Атрибуты:
            priority (float): Высокий приоритет для главных страниц.
            changefreq (str): Частота обновления (weekly).
    """
    priority = 1.0
    changefreq = 'weekly'

    def items(self):
        """
        Список имен URL-шаблонов для статичных страниц.
        """
        return ['home', 'contact', 'about']

    def location(self, item):
        """
        Возвращает URL по имени маршрута с помощью функции reverse.
        """
        return reverse(item)
