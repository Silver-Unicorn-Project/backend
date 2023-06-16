from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.db.models import Avg

from api.serializers import (
    CategoriesSerializer,
    CategoryDetailSerializer,
    ProductSerializer,
    ProductReviewSerializer,
    ArticlesSerializer
)
from products.models import Category, Products, Articles
from api.permissions import IsAuthorOrReadOnly


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
