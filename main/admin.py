# Импорт модуля admin из django.contrib.
# Этот модуль предоставляет функциональность административной панели Django.
from django.contrib import admin

# Импорт моделей Work и Service из текущего приложения (файл models.py).
# Эти модели будут зарегистрированы в административной панели для управления через веб-интерфейс.
from .models import Work, Service

# Регистрация модели Service в админке Django
admin.site.register(Service)

# Регистрация модели Work в админке Django
admin.site.register(Work)