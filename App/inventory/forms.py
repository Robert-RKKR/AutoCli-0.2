# Django Import:
from django.forms import ModelForm

# Application Import:
from .models.device import Device
from .models.color import Color
from .models.color import Credential
from .models.color import Group


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


class CredentialForm(ModelForm):

    class Meta:
        model = Credential
        fields = [
            'name', 'username', 'password', 'description',
        ]


class GroupForm(ModelForm):

    class Meta:
        model = Group
        fields = [
            'name', 'description', 'devices',
        ]
