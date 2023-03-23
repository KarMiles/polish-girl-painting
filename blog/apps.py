"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Class used to configure the blog application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
