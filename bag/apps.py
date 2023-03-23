"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.apps import AppConfig


class BagConfig(AppConfig):
    """
    Class used to configure the bag application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
