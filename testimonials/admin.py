"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Testimonial


# Models for testimonial management in admin page

@admin.register(Testimonial)
class TestimonialsAdmin(admin.ModelAdmin):
    """
    Admin class for the testimonial model.
    Section for managing testimonials.
    """
    list_display = (
        'title',
        'live',
        'created_on',
        )
    search_fields = [
        'title',
        'content',
        ]
    list_filter = (
        'live',
        )
