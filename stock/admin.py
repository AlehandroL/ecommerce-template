from django.contrib import admin

from .models import Stock

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['product', 'available', 'reserved', 'on_order', 'damaged', 'value']
