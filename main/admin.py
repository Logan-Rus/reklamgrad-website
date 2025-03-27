from django.contrib import admin
# Импорт моделей из текущего приложения (файл models.py)
from .models import (Work, Service, MainPage, MenuItem, ContactRequest)

class MenuItemInline(admin.TabularInline):
"""
    Встроенная админ-форма для модели MenuItem, используемая в админке MainPage.
    Позволяет редактировать пункты меню непосредственно на странице редактирования MainPage.
    
    Поля:
        - model (Model): Модель, для которой создается inline-форма (MenuItem).
        - extra (int): Количество дополнительных пустых форм для добавления новых пунктов меню.
    """
    model = MenuItem
    extra = 1 # Показывать 1 дополнительную пустую форму по умолчанию

@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
"""
    Административный интерфейс для модели MainPage.
    Включает встроенное редактирование связанных пунктов меню через MenuItemInline.
"""
    inlines = [MenuItemInline] # Добавляем возможность редактировать пункты меню "на месте"

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

# Регистрация остальных моделей
admin.site.register(Work)
admin.site.register(Service)
