from django.db import models
from django.db.models import F, Sum
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.utils.safestring import mark_safe

from phonenumber_field.modelfields import PhoneNumberField



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


class OrderQuerySet(models.QuerySet):

    def get_order_amount(self):
        amount_order = self.annotate(
            amount=Sum(F('order_items__quantity') *
                       F('order_items__product__price'))
        )
        return amount_order


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Пользователь',
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Статус',
        db_index=True,
    )
    phonenumber = PhoneNumberField(
        'Телефон',
        region='RU',
        db_index=True,
    )
    firstname = models.CharField('Имя', max_length=100)
    lastname = models.CharField('Фамилия', max_length=100)
    created_at = models.DateTimeField('Когда создан', auto_now=True)

    objects = OrderQuerySet.as_manager()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        verbose_name='Заказ',
        related_name='order_items',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Products,
        verbose_name='Товар',
        related_name='items',
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(
        'Количество',
        validators=[MinValueValidator(1)],
    )

    class Meta:
        verbose_name = 'Пункт заказа'
        verbose_name_plural = 'Пункты заказа'

    def __str__(self):
        return f'{self.product.name} {self.order.address}'


class Favorite(models.Model):
    title = models.CharField('Название', max_length=100)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favorites',
    )

    class Meta:
        verbose_name = 'Список избранного'
        verbose_name_plural = 'Списки избранного'

    def __str__(self):
        return f'{self.name}'


class FavoriteItem(models.Model):
    favorite = models.ForeignKey(
        Favorite,
        on_delete=models.CASCADE,
        verbose_name='Список избранного',
        related_name='favorites',
        db_index=True,
    )
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        verbose_name='Товар',
        related_name='favorite_items',
    )

    class Meta:
        verbose_name = 'Пункт избранного'
        verbose_name_plural = 'Пункты избранного'

    def __str__(self):
        return f'{self.product.name}'