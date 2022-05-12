from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from cart.forms import CartAddProductForm


def index(request, category_slug=None):
    category = None
    categories = Categories.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Categories, slug=category_slug)
        products = products.filter(category=category)
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'shop/index.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product_detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def all_products(request):
    products = Product.objects.all()
    return render(request, 'shop/all_products.html', {'products': products})


def about_us(request):
    return render(request, 'shop/about.html')
