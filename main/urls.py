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
    # - service_id: ID услуги
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),

    # Детальная страница работы
    # - work_id: ID работы
    path('works/<int:work_id>/', views.work_detail, name='work_detail'),

    # Страница со всеми работами
    path('works/', views.all_works, name='all_works'),

    # Страница со всеми услугами
    path('services/', views.all_services, name='all_services'),
]