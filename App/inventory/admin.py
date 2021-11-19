# Django Import:
from django.contrib import admin

# Application Import:
from .models.color import Color
from .models.credential import Credential
from .models.group import Group
from .models.device import Device

# Register Application models in Django Admin:
admin.site.register(Color)
admin.site.register(Credential)
admin.site.register(Group)
admin.site.register(Device)
