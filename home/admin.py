"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import HomeSettings


@admin.register(HomeSettings)
class SettingsAdmin(admin.ModelAdmin):
    """
    Admin class for managing home page settings.
    Show background image on home page.
    """
    list_display = (
        'background_image',)
