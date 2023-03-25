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


def shop():
    """
    Retrieve checkout settings from Checkout Settings in Admin page,
    present defaults if custom settings not available.
    Args:
        none
    Returns:
        delivery settings (dict)
    """
    if CheckoutSettings.objects.exists():
        # custom checkout settings
        checkout_settings = CheckoutSettings.objects.order_by('-id').first()
        delivery_settings = {
            'fdt': checkout_settings.free_delivery_threshold,
            'sdp': checkout_settings.standard_delivery_percentage,
            'dmc': checkout_settings.delivery_min_charge,
        }
    else:
        # default checkout settings
        delivery_settings = {
            'fdt': settings.FREE_DELIVERY_THRESHOLD,
            'sdp': settings.STANDARD_DELIVERY_PERCENTAGE,
            'dmc': settings.DELIVERY_MIN_CHARGE,
        }

    return delivery_settings


def bag_contents(request):
    """
    A context containing the bag contents
    Args:
        request (object): HTTP request object.
    Returns:
        The context with bag contents
    """
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    _shop = shop()
    fdt = _shop['fdt']
    sdp = _shop['sdp']
    dmc = _shop['dmc']

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if 0 < total < fdt:
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
        'free_delivery_threshold': fdt,
        'grand_total': grand_total,
    }

    return context
