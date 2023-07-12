from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from api.views import CategoryProductsViewSet
from products.views import *

schema_view = get_schema_view(
   openapi.Info(
      title="Silver Unicorn API",
      default_version='v1',
      description="Документация для конного магазина Silver Unicorn",
      contact=openapi.Contact(email="admin@silver_unicorn.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('', main_view, name='home'),
    path('card/<int:card_id>/', show_card, name='card'),
    path('buy_page/', buy_product, name='buy_page'),
    path('api/', include('api.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
       name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

