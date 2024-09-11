from django.shortcuts import render
from django.urls import reverse
import stripe
from django.conf import settings


#let's create a donation page

def donation_page(request):
    stripe.api_key = settings.STRIPE_PRIVATE_KEY
    sessions = stripe.checkout.Session.create(
        line_items=[{

            'price':'price_1PvWxSP6wf6niOUW0c9Rdiik',
            'quantity':1,
        }
        ],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('payment-success'))+ '?session_id={CHECKOUT_SESSION_ID}',
        # failure_url=request.build_absolute_uri(reverse('payment-failed')),
        )

    return render(request, 'donation/donation_page.html')

def payment_success(request):
    return render(request, 'donation/payment-success.html')

def payment_failed(request):

    return render(request, 'donation/payment-failure.html')