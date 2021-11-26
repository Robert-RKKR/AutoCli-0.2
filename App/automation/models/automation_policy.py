# Django Import:
from django.db import models
from django.utils.translation import gettext_lazy as _

# Applications Import:


# Model code:
class AutomationPolicy(models.Model):
    
    # Creation values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    status = models.BooleanField(default=False)
    root = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    # Main model values:
    name = models.CharField(max_length=16, blank=False, unique=True)
    description = models.CharField(max_length=512, default="Automation policy description")

    def __str__(self) -> str:
        return self.name


    # Meta sub class:
    class Meta:
        app_label = 'automation'