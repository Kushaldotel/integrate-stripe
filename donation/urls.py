from django.urls import path
from .import views

urlpatterns = [
    path('', views.donation_page, name='my-donation'),
    path('payment-success/', views.payment_success, name='payment-success'),
    path('payment-failed/', views.payment_failed, name='payment-failed'),
]
