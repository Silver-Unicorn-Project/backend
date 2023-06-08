from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from api.serializers import (
    CategoriesSerializer,
    CategoryDetailSerializer,
    ProductSerializer
)
from products.models import Category, Products


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
