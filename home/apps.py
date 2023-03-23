"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Class used to configure the home application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
