"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import uuid
from decimal import Decimal
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django_countries.fields import CountryField

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    """
    A class for a model for an order on the website
    """
    order_number = models.CharField(
        max_length=32,
        null=False,
        editable=False)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders')
    full_name = models.CharField(
        max_length=50,
        null=False,
        blank=False)
    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False)
    phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False)
    country = CountryField(
        blank_label="Country *",
        null=False,
        blank=False)
    postcode = models.CharField(
        max_length=20,
        null=True,
        blank=True)
    town_or_city = models.CharField(
        max_length=40,
        null=False,
        blank=False)
    street_address1 = models.CharField(
        max_length=80,
        null=False,
        blank=False)
    street_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True)
    county = models.CharField(
        max_length=80,
        null=True,
        blank=True)
    date = models.DateTimeField(
        auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0)
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0)
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0)
    original_bag = models.TextField(
        null=False,
        blank=False,
        default='')
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default='')

    def _generate_order_number(self):
        """
        Generate a random unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery cost
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0

        checkout_settings = CheckoutSettings.objects.order_by('-id').first()

        if checkout_settings:
            fdt = checkout_settings.free_delivery_threshold
            sdp = checkout_settings.standard_delivery_percentage
            dmc = checkout_settings.delivery_min_charge
        else:
            fdt = settings.FREE_DELIVERY_THRESHOLD
            sdp = settings.STANDARD_DELIVERY_PERCENTAGE
            dmc = settings.DELIVERY_MIN_CHARGE

        if self.order_total < fdt:
            self.delivery_cost = (
                max(
                    self.order_total * Decimal(sdp / 100),
                    dmc
                )
            )
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it has not been set already
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation of order number
        """
        return self.order_number


class OrderLineItem(models.Model):
    """
    A model for a website order line item
    """
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems')
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE)
    quantity = models.IntegerField(
        null=False,
        blank=False,
        default=0)
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'


class CheckoutSettings(models.Model):
    """
    Model for checkout settings
    These settings let authorized user activate / deactivate checkout
    and set custom delivery charges
    """
    class Meta:
        """
        Set up representation for Checkout settings on Admin page
        """
        verbose_name_plural = 'Settings'

    live = models.BooleanField(
        default=True)
    free_delivery_threshold = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True)
    standard_delivery_percentage = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True)
    delivery_min_charge = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True)
