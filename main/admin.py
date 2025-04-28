from django.contrib import admin
# Импорт моделей из текущего приложения (файл models.py)
from .models import (Work, Service, MainPage, MenuItem, ContactRequest, Footer, StaticPage, Advantage)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """
        Административный интерфейс для модели MenuItem (пункты меню).
        Настройки:
        - list_display: отображаемые поля в списке
        - list_editable: поле order доступно для редактирования прямо в списке
    """
    list_display = ['title', 'url', 'order']
    list_editable = ['order']  # Для удобной сортировки в админке

@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    """Стандартный интерфейс для главной страницы сайта"""
    pass


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    """
        Настроенный интерфейс для преимуществ компании с:
        - Сортировкой по полю order
        - Поиском по title и description
        - Отображением связанной главной страницы
    """
    list_display = ('title', 'order', 'main_page_short')
    list_editable = ('order',)
    search_fields = ('title', 'description')

    def main_page_short(self, obj):
        return obj.main_page.title if obj.main_page else '-'

    main_page_short.short_description = 'Главная страница'

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
    """
        Админ-интерфейс для статических страниц с:
        - Автозаполнением slug из title
        - Поиском по заголовку и содержанию
        - Сортировкой по заголовку
    """
    list_display = ('title', 'slug', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    ordering = ('title',)

# Регистрация остальных моделей
admin.site.register(Work)
admin.site.register(Service)
admin.site.register(Footer)