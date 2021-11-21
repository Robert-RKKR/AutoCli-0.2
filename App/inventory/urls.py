# Django Import:
from django.urls import path, re_path
from .views.device import *

urlpatterns = [
    path('device/add', add),
    re_path(r'^device/search/get$', search),
]