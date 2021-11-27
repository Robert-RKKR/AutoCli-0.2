# Django Import:
from django.forms import ModelForm

# Application Import:
from .models.device import Device
from .models.color import Color


# Forms:
class DeviceForm(ModelForm):

    class Meta:
        model = Device
        fields = [
            'status', 'name', 'hostname', 'device_type', 'credential', 'ico', 'ssh_port', 'https_port', 'description',
        ]


class ColorForm(ModelForm):

    class Meta:
        model = Color
        fields = [
            'name', 'value', 'description', 'devices', 'groups', 'credentials',
        ]