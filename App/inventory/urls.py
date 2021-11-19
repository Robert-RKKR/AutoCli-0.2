# Django Import:
from django.urls import path
from .views.device import device_add_one

urlpatterns = [
    path('device_add_one', device_add_one),
]