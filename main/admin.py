from django.contrib import admin
# Импорт моделей из текущего приложения (файл models.py)
from .models import (Work, Service, MainPage, MenuItem, ContactRequest, Footer, StaticPage)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'order']
    list_editable = ['order']  # Для удобной сортировки в админке

@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    """
    Настроенный административный интерфейс для модели ContactRequest.
    Обеспечивает удобный просмотр и фильтрацию контактных заявок.

    Поля:
        - list_display (tuple): Поля, отображаемые в списке заявок.
        - search_fields (tuple): Поля, по которым выполняется поиск.
        - list_filter (tuple): Поля, используемые для фильтрации списка.
    """
    list_display = ('email', 'message', 'created_at')
    search_fields = ('email', 'message')
    list_filter = ('created_at',)

@admin.register(StaticPage)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    ordering = ('title',)

# Регистрация остальных моделей
admin.site.register(Work)
admin.site.register(Service)
admin.site.register(Footer)