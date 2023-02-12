"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django import forms

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Testimonial


class PostTestimonial(forms.ModelForm):
    """
    Class for testimonial forms
    """
    class Meta:
        """
        Show indicated fields in the testimonial form
        """
        model = Testimonial
        fields = (
            'title',
            'content',
            )
