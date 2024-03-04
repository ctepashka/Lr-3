from django.contrib import admin
from django.urls import path
from .views import index, uslugi, address

urlpatterns = [
    path('', index),
    path('uslugi', uslugi),
    path('address', address),
]
