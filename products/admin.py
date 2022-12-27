from django.contrib import admin

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'excerpt',
        'description',
        'price',
        'priority',
        'available',
        'live',
        'image',
        'sku',
    )

    ordering = ('sku',)

    search_fields = [
        'title',
        'excerpt',
        'description']

    list_filter = (
        'available',
        'live',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
