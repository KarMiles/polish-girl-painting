from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


# custom class inheriting the built-in ClearableFileInput:
class CustomClearableFileInput(ClearableFileInput):
    # override the clear_checkbox_label:
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name =\
        'custom_widget_templates/custom_clearable_file_input.html'
