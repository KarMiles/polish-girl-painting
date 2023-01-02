from django.contrib import admin

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'orientation',
        'category',
        'excerpt',
        'price',
        'priority',
        'available',
        'live',
        'image',
        'highlight',
        'created_on',
        'updated_on',
        'sku',
    )

    ordering = ('sku',)

    search_fields = [
        'title',
        'excerpt',
        'description'
    ]

    list_filter = (
        'available',
        'live',
        'highlight',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
