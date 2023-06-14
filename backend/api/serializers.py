from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from products.models import Category, Products, ProductReview, Articles


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


class ProductReviewSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Products.objects.all(),
        required=False
    )
    author = SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = ('id', 'product', 'text', 'author', 'score', 'created')
        model = ProductReview

    def validate_score(self, value):
        if 0 > value > 5:
            raise serializers.ValidationError('Выберите оценку от 1 до 5')
        return value


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = (
            'title',
            'text',
            'created_at',
        )
