"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models


# Field choices

# Priority
PRIORITY_CHOICES = [
    ("1 - Top", "Top"),
    ("2 - High", "High"),
    ("3 - Normal", "Normal"),
    ("4 - Low", "Low"),
    ("5 - Lowest", "Lowest"),
]

# Orientation
ORIENTATION = [
    ("Landscape", "Landscape"),
    ("Portrait", "Portrait"),
    ("N/A", "Not Applicable")
]


# Models for products app


class Product(models.Model):
    """
    Class for the Product model
    representing items in Gallery
    """
    title = models.CharField(
        max_length=254,
        unique=True)
    sku = models.CharField(
        max_length=254,
        null=True,
        blank=True)
    excerpt = models.TextField(
        null=True,
        blank=True)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True)
    image = models.ImageField(
        null=True,
        blank=True)
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    orientation = models.CharField(
        max_length=9,
        choices=ORIENTATION,
        null=True,
        blank=True)
    is_unique = models.BooleanField(
        default=True)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="3 - Normal",
        null=True,
        blank=True)
    highlight = models.BooleanField(
        default=False)
    available = models.BooleanField(
        default=True)
    live = models.BooleanField(
        default=True)
    created_on = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True)
    updated_on = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True)

    class Meta:
        """
        Order products by priority and creation date
        """
        ordering = ['priority', 'created_on']

    def __str__(self):
        """
        Returns the product (item) title string
        Args:
            self (object): self.
        Returns:
            The product title string
        """
        return format(self.title)


class Category(models.Model):
    """
    Class for the Category model
    representing categories of products shown in Gallery
    """
    class Meta:
        """
        Sets plural representation and orders categories by name
        """
        verbose_name_plural = 'Categories'
        ordering = ['name']

    name = models.CharField(
        max_length=254)
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True)

    def __str__(self):
        return format(self.name)

    def get_friendly_name(self):
        """
        Friendly name for form iteration
        """
        return self.friendly_name
