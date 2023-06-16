from rest_framework import serializers

from products.models import Category, Products, Favorite


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


class FavoriteInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = (
            'name',
            'price',
            'size',
            'picture',
            'description',
        )


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = (
            'user',
            'products',
            'is_favorited',
        )

    def to_representation(self, instance):
        context = {'request': self.context.get('request')}
        return FavoriteInfoSerializer(instance.products, context=context).data
