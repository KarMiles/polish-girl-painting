"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    Admin class for managing product app.
    """
    list_display = (
        'title',
        'category',
        'price',
        'priority',
        'available',
        'highlight',
        'live',
        'created_on',
        'updated_on',
    )

    ordering = (
        'sku',
        'title',
        )

    search_fields = [
        'title',
        'excerpt',
        'description',
    ]

    list_filter = (
        'available',
        'live',
        'highlight',
        'orientation',
    )


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin class for managing product categories.
    Owner can add, delete and edit categories here.
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
