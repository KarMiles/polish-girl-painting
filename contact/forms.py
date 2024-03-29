"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django_contact_form.forms import ContactForm

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Contact


# Forms for contact app


class ContactForm(ContactForm):
    """
    Class for Contact form
    Set data, files, request and recipient_list initially to None
    """
    def __init__(
        self, *args, data=None, files=None,
            request=None, recipient_list=None, **kwargs):
        """
        For registered users
        pull email and full name or username from user
        """
        if request is not None and \
            request.method == 'GET' and \
                request.user.is_authenticated:
            kwargs['initial'] = {
                'email': request.user.email,
                'name': request.user.get_full_name() or request.user.username
            }
        super().__init__(*args, data, files, request, recipient_list, **kwargs)

    def save(self, fail_silently=False):
        """
        Save gathered data
        """
        data = self.get_message_dict()

        if self.request.user.is_authenticated:
            name = self.request.user
            contact_name = self.request.user.get_full_name()
        else:
            contact_name = self.cleaned_data.get("name")
            name = None

        Contact.objects.create(
            name=name,
            contact_name=contact_name,
            email=self.cleaned_data.get("email"),
            subject=data['subject'],
            body=data['message'])
        super().save(fail_silently=False)
