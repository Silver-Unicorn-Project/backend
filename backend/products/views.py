from django.shortcuts import get_object_or_404, render

from .models import Products, ProductsPicture


def main_view(request):
    cards = Products.objects.all()
    pic = ProductsPicture.objects.all()
    context = {
        'cards': cards,
        'pic': pic,
    }
    return render(request, 'products/base.html', context=context)


def show_card(request, card_id):
    card = get_object_or_404(Products, pk=card_id)
    pic = ProductsPicture.objects.all()
    context = {
        'card': card,
        'pic': pic,
    }
    return render(request, 'products/card_page.html', context=context)


def buy_product(request):
    card = Products.objects.all()
    pic = ProductsPicture.objects.all()
    context = {
        'card': card,
        'pic': pic,
    }
    return render(request, 'products/buy_page.html', context=context)
