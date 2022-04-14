from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'slug', 'price', 'in_stock', 'active', 'created_at', 'updated_at']
    list_filter = ['in_stock', 'active']
    list_editable = ['in_stock', 'active', 'price']
    prepopulated_fields = {'slug': ('name',)}
