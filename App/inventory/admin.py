# Django Import:
from django.contrib import admin

# Application Import:
from .models.color import Color

# Register Application models in Django Admin:
admin.site.register(Color)
