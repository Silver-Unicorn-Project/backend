from django.contrib import admin
from .models import *


class ProductsPictureAdmin(admin.StackedInline):
    model = ProductsPicture
    list_display = ('products', )


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    inlines = [ProductsPictureAdmin]
    list_display = ('name', 'description', 'price', 'quantity', 'is_published', 'created_at')
    list_display_links = ('name',)
    list_editable = ('is_published',)

    class Meta:
        model = Products


@admin.register(ProductsPicture)
class ProductsPictureAdmin(admin.ModelAdmin):
    pass
