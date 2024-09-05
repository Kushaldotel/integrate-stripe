from django.urls import path
from .import views

urlpatterns = [
    path('', views.donation_page, name='my-donation')
]
