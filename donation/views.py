from django.shortcuts import render

#let's create a donation page

def donation_page(request):
    return render(request, 'donation/donation_page.html')

def payment_success(request):
    return render(request, 'donation/payment-success.html')

def payment_failed(request):

    return render(request, 'donation/payment-failure.html')