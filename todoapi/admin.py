from django.contrib import admin
from .models import Category, Item
# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fields = ["title", "description", "category","completed", "user", "created_on", "due_date"]
    readonly_fields = ('created_on',)
    list_display = ["title", "created_on", "due_date", "category"]
    list_filter = ["due_date"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ["name"]
    list_display = ["name"]