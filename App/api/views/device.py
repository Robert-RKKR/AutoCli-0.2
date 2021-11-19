# Rest Django Import:
from rest_framework import generics

# Pagination's Import:
from ..pagination import (
    SmallResultsPagination,
    MediumResultsPagination,
    BigResultsPagination,
)

# Serializers Import:
from ..serializers import (
    DeviceGetSerializer,
)

# Application Import:
from inventory.models.device import Device

# ALL Device Views:
class DeviceAllAPI(generics.ListAPIView):
    queryset = Device.active.all()
    serializer_class = DeviceGetSerializer
    pagination_class = SmallResultsPagination
