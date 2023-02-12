"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Testimonial


# Models for blog management in admin page

@admin.register(Testimonial)
class TestimonialsAdmin(SummernoteModelAdmin):
    """
    Admin class for the blog model.
    Section for managing testimonials.
    """
    list_display = (
        'title',
        'live',
        'created_on',
        'updated_on')
    search_fields = [
        'title',
        'content']
    summernote_fields = ('content')
    list_filter = (
        'live',
        )
