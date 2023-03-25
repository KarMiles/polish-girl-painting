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
            'priority',
            'about_me',
            'live'
            )
        widgets = {
            'content': SummernoteWidget()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():  # pylint: disable=W0612
            field.widget.attrs['class'] = 'border-custom corners'
