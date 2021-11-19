# Django Import:
from django.forms import ModelForm

# Application Import:
from .models.device import Device


# Forms:
class DeviceAddOneForm(ModelForm):

    class Meta:
        model = Device
        fields = [
            'status','name', 'hostname', 'device_type', 'ico', 'ssh_port', 'https_port', 'description',
        ]