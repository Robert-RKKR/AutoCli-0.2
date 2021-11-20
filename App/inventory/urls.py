# Django Import:
from django.urls import path
from .views.device import *

urlpatterns = [
    path('device/add', add),
    path('device/search', search),
]