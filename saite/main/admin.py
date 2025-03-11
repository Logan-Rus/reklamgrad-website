from django.contrib import admin
from .models import Review, Collection

admin.site.register(Collection)
admin.site.register(Review)