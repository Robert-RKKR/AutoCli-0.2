# Django Import:
from django.urls import path
from .views.device import *

urlpatterns = [
    path('device_add_one', device_add_one),
    path('test', test),
]