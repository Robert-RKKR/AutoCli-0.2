# Django Import:
from django.db import models

# Model code:
class Color(models.Model):

    # Model values:
    name = models.CharField(max_length=32, blank=False, unique=True)

    # Model representation:
    def __str__(self) -> str:
        return self.name

    class Meta:
        app_label = 'inventory'