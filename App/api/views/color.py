# Rest Django Import:
from rest_framework import generics

# Pagination's Import:
from ..pagination import *

# Serializers Import:
from ..serializers import (
    ColorGetSerializer,
    ColorPostSerializer,
)

# Application Import:
from inventory.models.color import Color

# ALL Device Views:
class ColorAllAPI(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorGetSerializer
    pagination_class = SmallResultsPagination


class ColorAddAPI(generics.CreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorPostSerializer
