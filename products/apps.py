"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """
    Class used to configure the products application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
