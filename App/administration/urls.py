# Django Import:
from django.urls import path, re_path

# Views Import:
from .views import *


urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('login_page/', login_page, name='login_page'),
]