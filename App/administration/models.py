# Django Import:
from django.contrib.auth import get_user_model
from django.db import models

# Model code:
"""class Settings(models.Model):

    # Creation values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)"""

class Administrator(models.Model):

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    test_field = models.BooleanField(default=False)


    # Model representation:
    def __str__(self) -> str:
        return self.pk