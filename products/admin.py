from django.contrib import admin

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
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
