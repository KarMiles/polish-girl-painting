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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():  # pylint: disable=W0612
            field.widget.attrs['class'] = 'border-custom corners'
