"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django import forms
from django_summernote.widgets import SummernoteWidget
from .widgets import CustomClearableFileInput

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
        # fields = '__all__'
        fields = (
            # 'author',
            'title',
            'content',
            'highlight',
            'live',)
        widgets = {
            'content': SummernoteWidget()
        }

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput)
