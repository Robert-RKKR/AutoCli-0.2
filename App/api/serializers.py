# Rest Django Import:
from rest_framework import serializers

# Application Import:
from inventory.models.device import Device


# Serializers classes:
class DeviceGetSerializer(serializers.ModelSerializer):

    class Meta:
        app_label = 'api'
        model = Device
        fields = [
            'id',
            'created',
            'updated',
            'status',
            'ssh_status',
            'https_status',
            'name',
            'hostname',
            'device_type',
            'ico',
            'ssh_port',
            'https_port',
            'description',
            'credential',
            'secret',
            'token',
            'certificate',
        ]

