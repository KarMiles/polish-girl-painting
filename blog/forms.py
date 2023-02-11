"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django import forms
from django_summernote.widgets import SummernoteWidget

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .widgets import CustomClearableFileInput
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
            # 'author',
            'title',
            'content',
            'highlight',
            'live',
            'featured_image')
        widgets = {
            'content': SummernoteWidget()
        }

    featured_image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput)
