# Generated by Django 4.2 on 2023-06-12 15:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_category_slug_alter_products_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productreview',
            options={'ordering': ['created'], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AddField(
            model_name='productreview',
            name='score',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1, 'Минимум 1'), django.core.validators.MaxValueValidator(10, 'Максимум 10')], verbose_name='Рейтинг'),
        ),
        migrations.AddField(
            model_name='products',
            name='rating',
            field=models.IntegerField(null=True, verbose_name='Рейтинг'),
        ),
        migrations.AddConstraint(
            model_name='productreview',
            constraint=models.UniqueConstraint(fields=('product', 'author'), name='unique_product_author'),
        ),
    ]
