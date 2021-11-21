# Filters Import:
from django_filters import FilterSet

# Application Import:
from .models.device import Device


# Only name Filter Class:
class DeviceNameFilter(FilterSet):

    class Meta:
        model = Device
        fields = {
            'name': ['contains'],
        }

# Filter classes:
class DeviceFilter(FilterSet):

    class Meta:
        model = Device
        fields = {
            'status': ['exact'],
            'hostname': ['exact', 'contains'],
            'device_type': ['exact'],
            'ssh_status': ['exact'],
            'https_port': ['exact'],
        }
