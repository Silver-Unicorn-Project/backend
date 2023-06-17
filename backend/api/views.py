from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import (HTTP_201_CREATED, HTTP_204_NO_CONTENT,
                                   HTTP_400_BAD_REQUEST)
from django.db.models import Avg


from api.permissions import IsAuthorOrReadOnly
from api.serializers import (ArticlesSerializer, CategoriesSerializer,
                             CategoryDetailSerializer, FavoriteSerializer,
                             ProductReviewSerializer, ProductSerializer)
from products.models import Articles, Category, Favorite, Products
from users.models import User


class CategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = self.get_queryset().filter(category=None)
        serializer = CategoriesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, slug):
        queryset = self.get_queryset().filter(slug=slug)
        serializer = CategoryDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = Category.objects.select_related('category')
        return queryset


class ProductsViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.annotate(Avg("productreviews__score")).all()
    serializer_class = ProductSerializer


class CategoryProductsViewSet(viewsets.ViewSet):

    def list(self, request, slug):
        category_products = self.get_queryset().\
            filter(category__slug=slug).\
            filter(is_published=True)
        serializer = ProductSerializer(category_products, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = Products.objects.select_related('category')
        return queryset

    def favorite(self, request, slug=None, pk=None):
        user = User.objects.get(id=5)
        product = get_object_or_404(Products, pk=pk)
        obj = Favorite.objects.filter(user=user, products=product)
        if self.request.method == 'POST':
            if obj.exists():
                content = {'error': 'Этот товар уже есть в списке избранного'}
                return Response(content, status=HTTP_400_BAD_REQUEST)
            serializer = FavoriteSerializer(
                data={'user': user.pk, 'products': product.pk},
                context={'request': self.request},
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)

        if self.request.method == 'DELETE':
            if obj.exists():
                obj.delete()
                content = {'message': 'Товар удален из списка избранного'}
                return Response(content, status=HTTP_204_NO_CONTENT)
            content = {'error': 'Этого товара нет в избранном'}
            return Response(content, status=HTTP_400_BAD_REQUEST)


class ProductReviewViewSet(viewsets.ModelViewSet):

    serializer_class = ProductReviewSerializer
    permission_classes = (IsAuthorOrReadOnly)

    def get_queryset(self):
        product = get_object_or_404(Products, id=self.kwargs.get('product_id'))
        return product.productreviews.all()

    def perform_create(self, serializer):
        product_id = self.kwargs.get("product_id")
        product = get_object_or_404(Products, pk=product_id)
        serializer.save(author=self.request.user, product=product)


class ArticlesViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
