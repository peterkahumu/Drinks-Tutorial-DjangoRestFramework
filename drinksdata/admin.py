from django.contrib import admin
from .models import Drinks

# Register your models here.

@admin.register(Drinks)
class DrinksAdmin(admin.ModelAdmin):
    list_display = ['name', 'flavour', 'created_at']
    list_filter = ['flavour', 'created_at']
    ordering = ['created_at']
