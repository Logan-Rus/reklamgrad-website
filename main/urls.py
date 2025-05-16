 # Импорт функции path из django.urls.
# Функция path используется для создания URL-шаблонов в Django.
from django.urls import path
from django.views.generic.base import RedirectView
# Импорт модуля views из текущего приложения.
# В этом модуле находятся функции (представления), которые обрабатывают запросы и возвращают ответы.
from . import views
# Импорт обработчика sitemap из django.contrib.sitemaps.views
from django.contrib.sitemaps.views import sitemap
# Импорт классов sitemap для различных моделей
from .sitemaps import StaticPageSitemap, WorkSitemap, ServiceSitemap, StaticViewSitemap

# Словарь sitemap, где ключ — имя для sitemap в URL, значение — класс sitemap
sitemaps = {
    'static_pages': StaticPageSitemap,
    'works': WorkSitemap,
    'services': ServiceSitemap,
    'static_views': StaticViewSitemap,
}

# Определение URL-шаблонов для приложения
urlpatterns = [
    # Главная страница
    path('', views.home, name='home'),
    # Детальная страница услуги
    path('Usluga/<int:object_id>/', views.detail_view, {'model_name': 'service'}, name='service_detail'),
    # Детальная страница работы
    path('Portfolio/<int:object_id>/', views.detail_view, {'model_name': 'work'}, name='work_detail'),

    # Список всех услуг
    path('Nashi-Uslugi/', views.list_view, {'model_name': 'services'}, name='all_services'),
    # Список всех работ
    path('Portfolio/', views.list_view, {'model_name': 'works'}, name='all_works'),

    # Обработчик формы обратной связи
    path('contact-submit/', views.contact_submit, name='contact_submit'),

    # Редирект для robots.txt (файл для поисковых систем)
    path('robots.txt', RedirectView.as_view(url='/static/robots.txt')),

    # URL для sitemap.xml, который автоматически формируется из sitemap классов
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # Статические страницы
    path('<slug:slug>/', views.static_page_view, name='static_page'),
]