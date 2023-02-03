
"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django_summernote.widgets import SummernoteWidget
from django import forms

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Post


class PostForm(forms.ModelForm):
    """
    Class for blog forms
    """
    class Meta:
        """
        Show indicated fields in the blog form
        """
        model = Post
        fields = (
            'title',
            'content',
            'featured_image',
            'highlight',
            'live',)
        widgets = {
            'content': SummernoteWidget()
        }
