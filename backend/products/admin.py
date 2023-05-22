from django.contrib import admin
from .models import (
    Products,
    Status,
    Order,
    OrderItem,
    Favorite,
    FavoriteItem,
)


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'quantity',
        'size',
        'picture',
        'price',
        'is_published',
    )
    list_display_links = ('name',)
    search_fields = ('name',)
    list_editable = ('is_published',)


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
