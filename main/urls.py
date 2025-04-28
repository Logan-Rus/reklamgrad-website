 # Импорт функции path из django.urls.
# Функция path используется для создания URL-шаблонов в Django.
from django.urls import path

# Импорт модуля views из текущего приложения.
# В этом модуле находятся функции (представления), которые обрабатывают запросы и возвращают ответы.
from . import views

# Определение URL-шаблонов для приложения
urlpatterns = [
    # Главная страница
    path('', views.home, name='home'),
    # Детальная страница услуги
    path('service/<int:object_id>/', views.detail_view, {'model_name': 'service'}, name='service_detail'),
    # Детальная страница работы
    path('work/<int:object_id>/', views.detail_view, {'model_name': 'work'}, name='work_detail'),

    # Список всех услуг
    path('services/', views.list_view, {'model_name': 'services'}, name='all_services'),
    # Список всех работ
    path('works/', views.list_view, {'model_name': 'works'}, name='all_works'),

    # Обработчик формы обратной связи
    path('contact-submit/', views.contact_submit, name='contact_submit'),
    # Статические страницы
    path('<slug:slug>/', views.static_page_view, name='static_page'),

]