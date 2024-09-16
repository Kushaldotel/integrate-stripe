from django.shortcuts import render
from django.urls import reverse
import stripe
from django.conf import settings

from .models import Donation


#let's create a donation page

def donation_page(request):
    stripe.api_key = settings.STRIPE_PRIVATE_KEY
    session = stripe.checkout.Session.create(
        line_items=[{
            'price': 'price_1PvWxSP6wf6niOUW0c9Rdiik',
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('payment-success')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('payment-failed')),
    )
    donation = Donation.objects.get(id=1)

    context = {
        'stripe_session_id': session.id,  # Changed to match template variable
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,  # Changed to match template variable
        'donation': donation,
    }

    return render(request, 'donation/donation_page.html', context)


def payment_success(request):
    return render(request, 'donation/payment-success.html')

def payment_failed(request):

    return render(request, 'donation/payment-failure.html')