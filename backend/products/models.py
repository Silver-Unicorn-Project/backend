from django.db import models
from django.urls import reverse


class Products(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование товара')
    price = models.CharField(max_length=255, verbose_name='Цена')
    size = models.CharField(max_length=255, verbose_name='Размер', blank=True)
    picture = models.ImageField(upload_to='picture/%Y/%m/%d/', verbose_name='Фото')
    description = models.TextField(blank=True, verbose_name='Описание товара')
    quantity = models.IntegerField(verbose_name='Количество в наличии')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('card', kwargs={'card_id': self.pk})

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ('name', 'price')


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

