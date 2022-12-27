from django.shortcuts import render

from .models import Product


def all_products(request):
    """
    A view for all products
    including sorting and search queries
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

