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
    title = models.CharField(
        max_length=254,
        unique=True)
    excerpt = models.TextField(
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
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="3 - Normal",
        null=True,
        blank=True)
    available = models.BooleanField(
        default=True)
    highlight = models.BooleanField(
        default=False,
        null=True,
        blank=True)
    created_on = models.DateTimeField(
        auto_now_add=True)
    updated_on = models.DateTimeField(
        auto_now=True)
    live = models.BooleanField(
        default=False)

    class Meta:
        """
        Order products by priority
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
        return self.title
