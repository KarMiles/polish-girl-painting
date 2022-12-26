from django.db import models
from cloudinary.models import CloudinaryField

# Field choices

PRIORITY_CHOICES = [
    ("1 - Top", "Top"),
    ("2 - High", "High"),
    ("3 - Normal", "Normal"),
    ("4 - Low", "Low"),
    ("5 - Lowest", "Lowest"),
]


# Models for products app

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(
        max_length=254)
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(
        max_length=254,
        null=True,
        blank=True)
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    title = models.CharField(
        max_length=254,
        unique=True)
    excerpt = models.TextField(
        blank=True)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2)
    image = models.ImageField(
        null=True,
        blank=True)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="3 - Normal",
        null=True,
        blank=True)
    available = models.BooleanField(
        default=True)
    live = models.BooleanField(
        default=False)

    class Meta:
        """
        Order products by priority
        """
        ordering = ['priority']

    def __str__(self):
        """
        Returns the product (item) title string
        Args:
            self (object): self.
        Returns:
            The product title string
        """
        return self.title
