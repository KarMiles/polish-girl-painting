"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import PermissionDenied

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Testimonial
from .forms import TestimonialForm


# Views for testimonials app

class TestimonialList(generic.ListView):
    """
    A view to show testimonials
    Args:
        ListView: class based view
    Returns:
        Render of testimonials
    """
    model = Testimonial
    template_name = "testimonials.html"
    context_object_name = 'testimonials'

    def get_queryset(self):
        """
        Filters testimonials by the query
        Args:
            self (object): Self object
        Returns:
            testimonials with status live
            ordered by creation time
        """
        return Testimonial.objects.filter(
            live=True,
            user=self.request.user
            ).order_by("created_on")

    def get(self, *args, **kwargs):
        """
        Renders page with testimonials list
        Args:
            self (object): Self object
            **kwargs: **kwargs
        Returns:
            Render testimonial page
        """
        if not self.request.user.is_authenticated:
            raise PermissionDenied

        return render(
            self.request,
            "testimonial.html",
            {
                "testimonials": self.get_queryset(),
                "testimonial_form": TestimonialForm()
            },
        )

    def post(self, _request):
        """
        A view to save data gathered in testimonial form
        and show confirmation message.
        Args:
            self (object): Self object
            request
        Returns:
            Save data, show confirmation message,
            redirect to testimonial page after testimonial submit.
        """
        if not self.request.user.is_authenticated:
            raise PermissionDenied

        testimonial_form = TestimonialForm(data=self.request.POST)

        if testimonial_form.is_valid():
            testimonial_form.instance.user = self.request.user
            testimonial_form.save()
            messages.add_message(
                self.request,
                messages.INFO,
                'Testimonial request submitted!  We will respond shortly.')
            return redirect(reverse('testimonial'))

        return render(
            self.request,
            "testimonial.html",
            {
                "testimonials": self.get_queryset(),
                "testimonial_form": testimonial_form
            }
        )
