from django.contrib import admin
from .models import *

admin.site.register(Products)
admin.site.register(Status)
admin.site.register(Orders)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'size', 'picture', 'price')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_editable = ('is_published',)

