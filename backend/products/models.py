from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import F, Sum
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

from users.models import User


class Products(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Наименование товара'
    )
    price = models.DecimalField(
        'цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    size = models.CharField(
        max_length=255,
        verbose_name='Размер',
        blank=True
    )
    picture = models.FileField(
        blank=True,
        verbose_name='Изображениe товаров'
    )
    description = models.TextField('Описание товара')
    quantity = models.PositiveIntegerField('Количество в наличии')
    is_published = models.BooleanField(
        default=False,
        verbose_name='Публикация'
    )
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    category = models.ForeignKey(
        'Category',
        related_name='category_products',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Категории'
    )
    rating = models.IntegerField(
        verbose_name='Рейтинг',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ('name', 'price')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('card', kwargs={'card_id': self.pk})


class Category(models.Model):
    title = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name='Категории'
    )
    slug = models.SlugField('Слаг', unique=True)
    category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name='Категория',
        related_name='sub_categories',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


class ProductsPicture(models.Model):
    products = models.ForeignKey(
        Products,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        'Изображение',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Изображения товаров'
        verbose_name_plural = 'Изображения товаров'

    def __str__(self):
        return self.products.name


class Status(models.Model):
    status_name = models.CharField(
        max_length=255,
        verbose_name='Название статуса'
    )

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
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favorites',
    )
    products = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        verbose_name='Товары',
        related_name='favorites'
    )

    class Meta:
        verbose_name = 'Список избранного'
        verbose_name_plural = 'Списки избранного'

    def __str__(self):
        return f'{self.user.username}'


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


class ProductReview(models.Model):
    """Отзывы пользователей"""

    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name='productreviews',
        verbose_name='Отзывы',
        help_text='Оставьте свой отзыв'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='productreviews',
        help_text='Автор',
        null=False
    )
    text = models.TextField(
        verbose_name='Текст отзыва',
        help_text='Введите свой отзыв'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата отзыва'
    )
    score = models.PositiveIntegerField(
        verbose_name='Рейтинг',
        null=False,
        validators=(
            MinValueValidator(1, 'Минимум 1',),
            MaxValueValidator(5, 'Максимум 5',)
        ),
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['created']

        constraints = (
            models.UniqueConstraint(
                fields=('product', 'author',),
                name='unique_product_author'
            ),
        )

    def __str__(self):
        return self.text[:15]


class Articles(models.Model):
    title = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Наименование акции'
    )
    text = models.TextField(
        max_length=1000,
        verbose_name='Описание акции'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания акции'
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        max_length=200,
        unique=True,
        help_text='Введите слаг'
    )

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return self.title
