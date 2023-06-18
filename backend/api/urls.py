from django.urls import include, path

from api import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('categories/', views.CategoryViewSet.as_view({'get': 'list'})),
    path('categories/<str:slug>/', views.CategoryViewSet.as_view({'get': 'retrieve'})),
    path('<str:slug>/products/', views.CategoryProductsViewSet.as_view({'get': 'list'})),
    path('<str:slug>/products/<int:pk>/favorite/', 
         views.CategoryProductsViewSet.as_view(
             {'post': 'favorite', 'delete': 'favorite'}
         )),
    # путь для проверки пагинации (со всеми товарами)
    path('products/', views.CategoryProductsViewSet2.as_view({'get': 'list'})),
   ]