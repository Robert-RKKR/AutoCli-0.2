# Django Import:
from django.urls import path
from .views import *

urlpatterns = [
    # Device API:
    path('device/all', DeviceAllAPI.as_view(), name='device_all'),

    # Color API:
    path('color/all', ColorAllAPI.as_view(), name='color_all'),
    path('color/add', ColorAddAPI.as_view(), name='color_add'),
]