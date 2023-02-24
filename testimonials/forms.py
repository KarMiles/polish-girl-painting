"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django import forms
from django_summernote.widgets import SummernoteWidget

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
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
            'about_me',
            'live'
            )
        widgets = {
            'content': SummernoteWidget()
        }
