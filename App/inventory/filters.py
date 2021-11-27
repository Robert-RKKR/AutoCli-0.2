# Filters Import:
from django_filters import FilterSet

# Application Import:
from .models.device import Device
from .models.color import Color


class DeviceFilter(FilterSet):

    class Meta:
        model = Device
        fields = {
            'status': ['exact'],
            'hostname': ['exact', 'contains'],
            'credential': ['exact'],
            'device_type': ['exact'],
            'ssh_status': ['exact'],
            'https_port': ['exact'],
        }
