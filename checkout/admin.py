"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Order, OrderLineItem, CheckoutSettings


class OrderLineItemAdminInline(admin.TabularInline):
    """
    This inline item allows for adding and editing
    line items in the admin right from inside the order model.

    To add it to the order admin interface
    *inlines* option is added in the OrderAdmin class.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    A class to set up Order Admin page
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_bag',
        'stripe_pid',
    )

    fields = (
        'order_number',
        'user_profile',
        'date',
        'full_name',
        'email',
        'phone_number',
        'country',
        'postcode',
        'town_or_city',
        'street_address1',
        'street_address2',
        'county',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_bag',
        'stripe_pid',
    )

    list_display = (
        'order_number',
        'date',
        'full_name',
        'order_total',
        'delivery_cost',
        'grand_total',
    )

    ordering = ('-date',)


@admin.register(CheckoutSettings)
class SettingsAdmin(admin.ModelAdmin):
    """
    Class to set up e-commerce settings.
    When Live status ON checkout enabled, otherwise disabled.
    """
    list_display = (
        'live',
        'free_delivery_threshold',
        'standard_delivery_percentage',
        'delivery_min_charge',
    )


admin.site.register(Order, OrderAdmin)
