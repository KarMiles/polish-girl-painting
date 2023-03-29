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
        'priority',
        'created_on',
        'updated_on')
    search_fields = [
        'title',
        'content']
    list_filter = (
        'live',)

    actions = ['make_live', 'make_not_live']

    def make_live(self, _request, queryset):
        """
        Change status of a post to live (live True)
        """
        queryset.update(live=True)

    def make_not_live(self, _request, queryset):
        """
        Change status of a post to live (live True)
        """
        queryset.update(live=False)
