from django.contrib import admin
from .models import *


class ProductsPictureAdmin(admin.StackedInline):
    model = ProductsPicture
    list_display = ('products',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    inlines = [ProductsPictureAdmin]
    list_display = ('name', 'description', 'cat', 'price', 'quantity', 'is_published', 'created_at')
    list_display_links = ('name',)
    list_editable = ('is_published',)

    class Meta:
        model = Products


@admin.register(ProductsPicture)
class ProductsPictureAdmin(admin.ModelAdmin):
    pass
