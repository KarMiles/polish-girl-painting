"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .forms import ContactForm


class ContactFormView(FormView):
    """
    View to show confirmation message after recording the message.

    """
    form_class = ContactForm
    success_url = reverse_lazy("contact")
    template_name = "django_contact_form/contact_form.html"

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            messages.INFO,
            'Message recorded successfully!')
        return super().form_valid(form)
