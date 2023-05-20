from django.shortcuts import render, get_object_or_404
from .models import *


def main_view(request):
    cards = Products.objects.all()
    context = {
        'cards': cards,
    }
    return render(request, 'products/base.html', context=context)


def show_card(request, card_id):
    card = get_object_or_404(Products, pk=card_id)
    context = {
        'card': card,
    }
    return render(request, 'products/card_page.html', context=context)


def buy_product(request):
    card = Products.objects.all()
    context = {
        'card': card,
    }
    return render(request, 'products/buy_page.html', context=context)
