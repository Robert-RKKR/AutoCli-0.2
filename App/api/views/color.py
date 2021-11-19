# Rest Django Import:
from rest_framework import generics

# Pagination's Import:
from ..pagination import *

# Serializers Import:
from ..serializers import (
    ColorGetSerializer,
)

# Application Import:
from inventory.models.color import Color

# ALL Device Views:
class ColorAllAPI(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorGetSerializer
    pagination_class = SmallResultsPagination
