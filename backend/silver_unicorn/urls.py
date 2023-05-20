from django.contrib import admin
from django.urls import path
from products.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='home'),
    path('card/<int:card_id>/', show_card, name='card'),
    path('buy_page/', buy_product, name='buy_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)