"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django import forms
from allauth.account.adapter import get_adapter

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
            'live'
            )
