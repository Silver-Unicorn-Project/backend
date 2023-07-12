from django.contrib import admin
from django.utils.html import format_html

from .models import (Articles, Category, Favorite, FavoriteItem, Order,
                     OrderItem, ProductReview, Products, ProductsPicture,
                     Status)


class ProductsPictureAdmin(admin.StackedInline):
    model = ProductsPicture
    list_display = ('products',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'quantity',
        'size',
        'picture',
        'price',
        'rating',
        'is_published',
    )
    list_display_links = ('name',)
    list_editable = ('is_published',)

    def get_html_picture(self, objects):
        if objects.picture:
            return format_html(f"<img src='{objects.picture.url}' height='200px' />")

    get_html_picture.short_description = 'Миниатюра'

    class Meta:
        model = Products


# @admin.register(ProductsPicture)
# class ProductsPictureAdmin(admin.ModelAdmin):
#     pass


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'firstname',
        'lastname',
    )
    save_on_top = True
    inlines = (
        OrderItemInline,
    )


class FavoriteItemInline(admin.TabularInline):
    model = FavoriteItem
    extra = 0


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    inlines = (
        FavoriteItemInline,
    )
    list_display = (
        'user',
        'products',
    )
    search_fields = (
        'user',
    )


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    """
    Интерфейс отзывов на странице сайта.
    """

    list_display = (
        'pk',
        'product',
        'author',
        'text',
        'created',
        'score',
    )
    search_fields = ('text',)
    list_filter = ('product', 'score')
    empty_value_display = '-пусто-'


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    """
    Интерфейс акций на странице сайта.
    """

    list_display = (
        'pk',
        'title',
        'text',
        'created_at',
        'slug',
    )
    search_fields = ('created_at',)
    list_filter = ('title',)
    empty_value_display = '-пусто-'
    prepopulated_fields = {"slug": ("title",)}
