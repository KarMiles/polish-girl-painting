"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from products.models import Product
from checkout.models import CheckoutSettings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    checkout_settings = CheckoutSettings.objects.order_by('-id').first()
    fdt = checkout_settings.free_delivery_threshold
    sdp = checkout_settings.standard_delivery_percentage
    dmc = checkout_settings.delivery_min_charge

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < fdt and total > 0:
        delivery = max(
            total * Decimal(sdp / 100),
            dmc)
        free_delivery_delta = fdt - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': CheckoutSettings.free_delivery_threshold,
        'grand_total': grand_total,
    }

    return context
