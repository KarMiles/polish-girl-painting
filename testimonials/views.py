"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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
        Render page with a list of testimonials
        Posts ordered by priority and date of creation
        Non-staff users see live (aproved) testimonials only
        Staff users see live and unapproved testimonials
    """
    model = Testimonial

    testimonials = Testimonial.objects.all()

    template_name = 'testimonials/testimonials.html'
    ordering = ['priority', 'created_on']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(live=True)


def testimonial_detail(request, testimonial_id):
    """
    A view to show individual testimonial details
    """

    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)

    context = {
        'testimonial': testimonial,
    }

    return render(request, 'testimonials/testimonial_detail.html', context)


@login_required
def testimonial_add(request):
    """ Add a testimonial to the store """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only registered users can do that.')
        return redirect(reverse('home'))

    # POST handler:
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            testimonial = form.save()
            messages.success(
                request,
                'Thank you for sharing!')
            return redirect(
                reverse(
                    'testimonial_detail',
                    args=[testimonial.id]))
        else:
            messages.error(
                request,
                'Failed to add testimonial. Please ensure the form is valid.')
    else:
        form = TestimonialForm()

    template = 'testimonials/testimonial_add.html'
    context = {
        'form': form,
        'hide_bag_toast': True
    }

    return render(request, template, context)


@login_required
def testimonial_edit(request, testimonial_id):
    """ Edit a testimonial in the store """
    if not request.user.is_authorized:
        messages.error(
            request,
            'Sorry, only authorized users can do that.')
        return redirect(
            reverse('home'))

    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)

    # POST handler
    if request.method == 'POST':
        form = TestimonialForm(
            request.POST,
            request.FILES,
            instance=testimonial)
        if form.is_valid():
            testimonial = form.save()
            messages.success(
                request,
                'Successfully updated Testimonial!')
            return redirect(
                reverse(
                    'testimonial_detail',
                    args=[testimonial.id]))
        else:
            messages.error(
                request,
                'Failed to update testimonial. \
                    Please ensure the form is valid.')
    else:
        form = TestimonialForm(instance=testimonial)
        messages.info(
            request,
            f'You are editing {testimonial.title}')

    template = 'testimonials/testimonial_edit.html'
    context = {
        'form': form,
        'testimonial': testimonial,
        'hide_bag_toast': True
    }

    return render(request, template, context)


@login_required
def testimonial_delete(request, testimonial_id):
    """ Delete a testimonial from the list """
    if not request.user.is_authenticated:
        messages.error(
            request,
            'Sorry, only authorised users can do that.')
        return redirect(reverse('home'))

    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    testimonial.delete()
    messages.success(request, 'Testimonial deleted!')

    template = 'testimonials/testimonials.html'
    context = {
        'hide_bag_toast': True
    }

    return render(request, template, context)
