# Django Import:
from django.contrib import admin

# Application Import:
from .models.color import (
    ColorDeviceRelation,
    ColorGroupRelation,
    ColorCredentialRelation,
    Color,
)
from .models.group import (
    GroupDeviceRelation,
    Group,
)
from .models.credential import Credential
from .models.device import Device

# Register Application models in Django Admin:
admin.site.register(Color)
admin.site.register(ColorDeviceRelation)
admin.site.register(ColorGroupRelation)
admin.site.register(ColorCredentialRelation)
admin.site.register(Credential)
admin.site.register(Group)
admin.site.register(GroupDeviceRelation)
admin.site.register(Device)
