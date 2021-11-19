# Django Import:
from django.urls import path
from .views.device import DeviceAllAPI

urlpatterns = [
    # Device API:
    path('device/all', DeviceAllAPI.as_view(), name='device_all'),
]