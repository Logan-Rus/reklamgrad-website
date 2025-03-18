# Импорт модуля admin из django.contrib.
# Этот модуль предоставляет функциональность административной панели Django.
from django.contrib import admin

# Импорт функций include и path из django.urls.
# - path: используется для создания URL-шаблонов.
# - include: позволяет включать URL-шаблоны из других приложений.
from django.urls import include, path

# Импорт модуля settings из django.conf.
# Этот модуль предоставляет доступ к настройкам проекта (settings.py).
from django.conf import settings

# Импорт функции static из django.conf.urls.static.
# Эта функция используется для обслуживания медиафайлов в режиме разработки.
from django.conf.urls.static import static

# Основные URL-шаблоны проекта
urlpatterns = [
    # Административная панель Django
    path('admin/', admin.site.urls),

    # Подключение URL-шаблонов из приложения 'main'
    path('', include('main.urls')),
]

# Добавление поддержки медиафайлов в режиме разработки
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Дополнительная проверка: если проект находится в режиме DEBUG,
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)