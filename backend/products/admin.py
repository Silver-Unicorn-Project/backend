from django.contrib import admin

from .models import (
    Products,
    Status,
    Order,
    OrderItem,
    Favorite,
    FavoriteItem,
)


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
    list_display = ('name', 'cat', 'price', 'quantity', 'is_published', 'created_at', 'get_html_picture')

    
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
    list_editable = ('is_published',)

    def get_html_picture(self, objects):
        if objects.picture:
            return mark_safe(f"<img src='{objects.picture.url}' width=100")

    get_html_picture.short_description = 'Миниатюра'

    class Meta:
        model = Products


@admin.register(ProductsPicture)
class ProductsPictureAdmin(admin.ModelAdmin):
    pass


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