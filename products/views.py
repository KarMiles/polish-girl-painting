from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
# from django.db.models.functions import Lower

from .models import Product, Category


def all_products(request):
    """
    A view for all products
    including sorting and search queries
    """

    products = Product.objects.all()
    query = None
    categories = None
    orientations = None

    if request.GET:

        # Filter by category
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Filter by orientation TODO
        if 'orientation' in request.GET:
            orientations = request.GET['orientation']
            products = products.filter(orientation__in=orientations)
            orientations = Product.objects.filter(orientation__in=orientations)

        # Search functionality
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    "Enter search criteria!")
                return redirect(reverse('products'))

            queries = Q(title__icontains=query) | \
                Q(excerpt__icontains=query) | \
                Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_orientations': orientations,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual product details
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
