from django.urls import path, include

from api import views


urlpatterns = [
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('categories/', views.CategoryViewSet.as_view({'get': 'list'})),
    path('categories/<str:slug>/', views.CategoryViewSet.as_view({'get': 'retrieve'})),
    path('<str:slug>/products/', views.CategoryProductsViewSet.as_view({'get': 'list'}))
]
