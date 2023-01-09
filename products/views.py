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
    available = None
    availability = None
    orientation = None
    orientations = None
    categories = None
    highlights = None

    if request.GET:

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

        # Filter by availability
        if 'available' in request.GET:
            available = request.GET['available']
            availability = request.GET['available'].split(',')
            products = products.filter(available__in=availability)
            availability = Product.objects.filter(available__in=availability)

        # Filter by orientation
        if 'orientation' in request.GET:
            orientation = request.GET['orientation']
            orientations = request.GET['orientation'].split(',')
            products = products.filter(orientation__in=orientations)
            orientations = Product.objects.filter(orientation__in=orientations)

        # Filter by category
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Filter highlights
        if 'highlight' in request.GET:
            highlights = request.GET['highlight'].split(',')
            products = products.filter(highlight__in=highlights)
            highlights = Product.objects.filter(highlight__in=highlights)

    context = {
        'products': products,
        'search_term': query,
        'available': available,
        'current_availability': availability,
        'orientation': orientation,
        'current_orientations': orientations,
        'current_categories': categories,
        'highlights': highlights,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual product details
    """

    product = get_object_or_404(Product, pk=product_id)

    bag = request.session.get('bag', {})

    product_in_bag = str(product_id) in bag.keys()

    context = {
        'product': product,
        'product_in_bag': product_in_bag

    }

    return render(request, 'products/product_detail.html', context)

