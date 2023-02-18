"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Product, Category
from .forms import ProductForm


# Views for products app

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

    product_is_in_bag = str(product_id) in bag.keys()

    context = {
        'product': product,
        'product_is_in_bag': product_is_in_bag

    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    # POST handler:
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/product_add.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    # POST handler
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.title}')

    template = 'products/product_edit.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


class DeleteProduct(generic.DeleteView):
    """
    A view to delete a product
    Args:
        DeleteView: generic class based view
    Returns:
        Request confirmation of product deletion
        Redirect to products page after delete
    """
    success_url = reverse_lazy('products')
    queryset = Product.objects.all()
    template_name = 'products/product_delete_confirm.html'

    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object,
        then redirect to the success URL
        and show confirmation message.
        """
        self.object = self.get_object()  \
            # pylint: disable=attribute-defined-outside-init

        success_url = self.get_success_url()
        self.object.delete()

        messages.add_message(
            self.request,
            messages.INFO,
            'Product deleted successfully!')

        return HttpResponseRedirect(success_url)
