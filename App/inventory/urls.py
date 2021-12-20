# Django Import:
from django.urls import path, re_path
from .views.device import *
from .views.credential import *
from .views.group import *
from .views.color import *
from .views.test import test

urlpatterns = [
    path('test', test, name='test'),

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

    # ------------------ CREDENTIAL ------------------ #
    re_path(r'^credential/search/get?$', CredentialSearchView.as_view(), name='credential_search'),
    path('credential/add', CredentialAddView.as_view(), name='credential_add'),
    path('credential/one/<int:pk>', CredentialOneView.as_view(), name='credential_one'),
    path('credential/update/<int:pk>', CredentialUpdateView.as_view(), name='credential_update'),
    path('credential/delete/<int:pk>', CredentialDeleteView.as_view(), name='credential_delete'),

    # ------------------ GROUP ------------------ #
    re_path(r'^group/search/get?$', GroupSearchView.as_view(), name='group_search'),
    path('group/add', GroupAddView.as_view(), name='group_add'),
    path('group/one/<int:pk>', GroupOneView.as_view(), name='group_one'),
    path('group/update/<int:pk>', GroupUpdateView.as_view(), name='group_update'),
    path('group/delete/<int:pk>', GroupDeleteView.as_view(), name='group_delete'),
]