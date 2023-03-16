"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Contact

# Admin model for contact app


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin class for the contact model.
    """
    list_display = ('name', 'contact_name', 'email', 'body', 'created_on')
    search_fields = ['name', 'contact_name', 'body', ]
    list_filter = ('created_on',)
    list_display_links = ('body',)
