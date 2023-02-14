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
from django.db.models import Q

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Testimonial
from .forms import TestimonialForm


# Views for testimonials app

def all_testimonials(request):
    """
    A view for all testimonials
    including sorting and search queries
    """
    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'testimonials/testimonials.html', context)


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
def add_testimonial(request):
    """ Add a testimonial to the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    # POST handler:
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save()
            messages.success(request, 'Successfully added testimonial!')
            return redirect(reverse('testimonial_detail', args=[testimonial.id]))
        else:
            messages.error(
                request,
                'Failed to add testimonial. Please ensure the form is valid.')
    else:
        form = TestimonialForm()

    template = 'testimonials/testimonial_add.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_testimonial(request, testimonial_id):
    """ Edit a testimonial in the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)

    # POST handler
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            testimonial = form.save()
            messages.success(request, 'Successfully updated testimonial!')
            return redirect(reverse('testimonial_detail', args=[testimonial.id]))
        else:
            messages.error(
                request,
                'Failed to update testimonial. Please ensure the form is valid.')
    else:
        form = TestimonialForm(instance=testimonial)
        messages.info(request, f'You are editing {testimonial.title}')

    template = 'testimonials/testimonial_edit.html'
    context = {
        'form': form,
        'testimonial': testimonial,
    }

    return render(request, template, context)


class DeleteTestimonial(generic.DeleteView):
    """
    A view to delete a testimonial
    Args:
        DeleteView: generic class based view
    Returns:
        Request confirmation of testimonial deletion
        Redirect to testimonials page after delete
    """
    success_url = reverse_lazy('testimonials')
    queryset = Testimonial.objects.all()
    template_name = 'testimonials/testimonial_delete_confirm.html'

    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object,
        then redirect to the success URL
        and show confirmation message.
        """
        self.object = self.get_object()  \
            # pylint: disable=attribute-defined-outside-init

        success_url = self.get_success_url()
        self.object.delete()

        messages.add_message(
            self.request,
            messages.INFO,
            'Post deleted successfully!')

        return HttpResponseRedirect(success_url)
