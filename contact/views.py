"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render
from django.views.generic.edit import FormView

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .forms import ContactForm


class ContactFormView(FormView):
    """
    View which can render and send email from a contact form.

    """
    form_class = ContactForm
    recipient_list = None
    success_url = reverse_lazy("django_contact_form_sent")
    template_name = "django_contact_form/contact_form.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        # ContactForm instances require instantiation with an
        # HttpRequest.
        kwargs = super().get_form_kwargs()
        kwargs.update({"request": self.request})

        # We may also have been given a recipient list when
        # instantiated.
        if self.recipient_list is not None:
            kwargs.update({"recipient_list": self.recipient_list})
        return kwargs
