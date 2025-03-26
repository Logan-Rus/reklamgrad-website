from django.contrib import admin
from .models import (Work, Service, MainPage, MenuItem, ContactRequest)

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1

@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'message', 'created_at')
    search_fields = ('email', 'message')
    list_filter = ('created_at',)

# Простая регистрация остальных моделей
admin.site.register(Work)
admin.site.register(Service)