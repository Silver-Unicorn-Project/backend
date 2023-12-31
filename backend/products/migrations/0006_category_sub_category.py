# Generated by Django 4.2 on 2023-06-07 15:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_products_cat_remove_productspicture_pictures_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='products.category', verbose_name='Категория'),
        ),
    ]
