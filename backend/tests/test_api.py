from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.serializers import ProductSerializer
from products.models import Products


class ProductsAPITestCase(APITestCase):
    def test_get(self):
        product_1 = Products.objects.create(
            name='Шлем1',
            price=500,
            size='S',
            description='Заебатый шлем',
            quantity = 1,
            rating = 1
        )
        product_2 = Products.objects.create(
            name='Шлем2',
            price=500,
            size='S',
            description='Заебатый шлем',
            quantity = 1,
            rating = 1
        )
        url = reverse('products-list')
        response = self.client.get(url)
        serializer_data = ProductSerializer(product_1, product_2, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        # self.assertEqual(serializer_data, response.data)

