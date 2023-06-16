from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('products', views.ProductsViewSet, basename='products')


urlpatterns = [
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('categories/', views.CategoryViewSet.as_view({'get': 'list'})),
    path('categories/<str:slug>/', views.CategoryViewSet.as_view({'get': 'retrieve'})),
    path('<str:slug>/products/', views.CategoryProductsViewSet.as_view({'get': 'list'})),
    path('', include(router.urls))
   ]
