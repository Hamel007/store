from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, CreateView

from .models import Product, Cart, CartItem


class ProductsList(ListView):
    """Список всех продуктов"""
    model = Product
    template_name = "shop/list-product.html"


class ProductDetail(DetailView):
    """Карточка товара"""
    model = Product
    context_object_name = 'product'
    template_name = 'shop/product-detail.html'


@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(customer=instance, id=instance.id)


def cart_view(request):
    prod = CartItem.objects.first()
    contex = {"prod": prod
              }
    return render(request, 'shop/cart.html', contex)


def add_cart_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    new_item = CartItem.objects.get_or_create(product=product)
    cart = Cart.objects.first()
    if new_item not in cart.item.all():
        cart.items.add(new_item)
        cart.seve()
        return (request, cart)



