# Django Import:
from django.urls import path, re_path
from .views.device import *

urlpatterns = [
    re_path('device/test/', test),
    re_path('device/test2/', TestView.as_view()),
    re_path('device/add/', add),
    path('device/edit/<int:pk>', edit),
    path('device/one/<int:pk>', one),
    re_path(r'^device/search/get$', search),
]