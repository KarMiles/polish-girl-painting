"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import json
import stripe
from django.shortcuts import render, redirect, reverse, \
    get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from products.models import Product
from bag.contexts import bag_contents
from .models import Order, OrderLineItem, CheckoutSettings
from .forms import OrderForm


@require_POST
def cache_checkout_data(request):
    """
    This function caches the bag, order and user data and catches an error
    if it doesn't go through.
    Args:
        request (object)
    Returns:
        A HTTP response with the relevant status and a message.
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def full_name_from_last_order(request):
    """
    If full name not existent in User profile,
    attempt to get it from last order
    Args:
        request (object): request.
    Returns:
        Full name string.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    result = ""

    if orders:
        result = orders.last().full_name

    return result


def checkout(request):
    """
    This function processes the checkout:
    the bag contents, user info and the payment, with validation.
    Args:
        request (object)
    Returns:
        The request object, the checkout template and the context.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        # if no full name in profile attempt to get from last order:
        if request.POST['full_name']:
            full_name = request.POST['full_name']
        else:
            full_name = full_name_from_last_order(request)

        form_data = {
            'full_name': full_name,
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag\
                            wasn't found in our database.\
                            Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number]))

        messages.error(request, 'There was an error with your form. \
            Please check your information.')

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(
                request,
                "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the form with info from user profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)

                # if no full name in profile attempt to get from last order:
                if profile.user.get_full_name():
                    full_name = profile.user.get_full_name()
                else:
                    full_name = full_name_from_last_order(request)

                order_form = OrderForm(initial={
                    'full_name': full_name,
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    checkout_live_setting = CheckoutSettings.objects.order_by('-id').first()
    checkout_is_live = checkout_live_setting is None \
        or checkout_live_setting.live

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'checkout_is_live': checkout_is_live,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save user info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    # Change product available status to false
    bag = request.session.get('bag', {})

    for item_id in bag.items():
        for id_number in item_id:
            try:
                product = Product.objects.get(id=id_number)
                if product.is_unique:
                    product.available = False
                    product.save()

            except Product.DoesNotExist:
                messages.error(request, (
                    "Product availability needs to be checked. \
                        Please contact me directly!")
                )

    # Confirmation message
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
