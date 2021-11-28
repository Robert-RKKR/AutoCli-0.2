# Filters Import:
from django_filters import FilterSet

# Application Import:
from .models.device import Device
from .models.color import Color
from .models.color import Credential
from .models.color import Group


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


class ColorFilter(FilterSet):

    class Meta:
        model = Color
        fields = {
            'value': ['contains'],
            'description': ['contains'],
            'devices': ['contains'],
            'groups': ['contains'],
            'credentials': ['contains'],
        }



class CredentialFilter(FilterSet):

    class Meta:
        model = Credential
        fields = {
            'username': ['exact'],
            'description': ['contains'],
        }


class GroupFilter(FilterSet):

    class Meta:
        model = Group
        fields = {
            'description': ['contains'],
            'devices': ['contains'],
        }