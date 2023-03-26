"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """
    Display the user's profile.
    Args:
        request (object): HTTP request object.
    Returns:
        Render user profile with update confirmation message.
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    # POST handler:
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request,
                ('Update failed. Please make sure the form is valid.'))
    else:
        form = UserProfileForm(instance=user_profile)

    orders = user_profile.orders.order_by('-date').all()

    if orders:
        full_name_from_last_order = orders.last().full_name
    else:
        full_name_from_last_order = ""

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'full_name': full_name_from_last_order,
        'hide_bag_toast': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    A view to update order history for the user
    Args:
        request (object): HTTP request object,
        order_number (string): order number.
    Returns:
        Success message,
        Render user's order history.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
