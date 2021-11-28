# Django Import:
from django.urls import path, re_path
from .views.device import *
from .views.color import *

urlpatterns = [
    # ------------------ DEVICE ------------------ #
    re_path(r'^device/search/get?$', DeviceSearchView.as_view(), name='device_search'),
    path('device/add/', DeviceAddView.as_view(), name='device_add'),
    path('device/one/<int:pk>', DeviceOneView.as_view(), name='device_one'),
    path('device/update/<int:pk>', DeviceUpdateView.as_view(), name='device_update'),
    path('device/delete/<int:pk>', DeviceDeleteView.as_view(), name='device_delete'),

    # ------------------ COLOR ------------------ #
    re_path(r'^color/search/get?$', ColorSearchView.as_view(), name='color_search'),
    path('color/add', ColorAddView.as_view(), name='color_add'),
    path('color/one/<int:pk>', ColorOneView.as_view(), name='color_one'),
    path('color/update/<int:pk>', ColorUpdateView.as_view(), name='color_update'),
    path('color/delete/<int:pk>', ColorDeleteView.as_view(), name='color_delete'),
]