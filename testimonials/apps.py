"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.apps import AppConfig


class TestimonialsConfig(AppConfig):
    """
    Class used to configure the testimonials application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'testimonials'
