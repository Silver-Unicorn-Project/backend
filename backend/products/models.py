from django.db import models
from django.urls import reverse


class Products(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Наименование товара')
    price = models.PositiveIntegerField(verbose_name='Цена')
    size = models.CharField(max_length=255, verbose_name='Размер', blank=True)
    picture = models.FileField(blank=True, verbose_name='Изображениe товаров')
    description = models.TextField(max_length=1000, verbose_name='Описание товара')
    quantity = models.PositiveIntegerField(verbose_name='Количество в наличии')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категории')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('card', kwargs={'card_id': self.pk})

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ('name', 'price')


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)


class ProductsPicture(models.Model):
    products = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    pictures = models.FileField(upload_to='picture/')

    def __str__(self):
        return self.products.name

    class Meta:
        verbose_name = 'Изображения товаров'
        verbose_name_plural = 'Изображения товаров'


class Status(models.Model):
    status_name = models.CharField(max_length=255, verbose_name='Название статуса')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Orders(models.Model):
    data = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Имя')
    phone = models.CharField(max_length=200, verbose_name='Телефон')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
