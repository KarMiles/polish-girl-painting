"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django import forms

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Testimonial, AboutMe


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
            'live'
            )


class AboutMeForm(forms.ModelForm):
    """
    Class for About Me section form
    """
    class Meta:
        """
        Show indicated fields in the aboutme form
        """
        model = AboutMe
        fields = (
            'title',
            'content',
            'live'
            )
