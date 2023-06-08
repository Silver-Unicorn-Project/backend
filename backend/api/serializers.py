from rest_framework import serializers

from products.models import Category, Products


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', )


class CategoryDetailSerializer(serializers.ModelSerializer):
    sub_categories = CategoriesSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ('sub_categories', )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = (
            'name',
            'price',
            'description',
            'quantity',
        )
