# Django Import:
from django.db import models
from django.utils.translation import gettext_lazy as _

# Applications Import:
from .automation_policy import AutomationPolicy


# Model code:
class TaskManager(models.Model):

    # Creation values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    status = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    # Automation policy data:
    automation_policy = models.ForeignKey(AutomationPolicy, on_delete=models.PROTECT)

    # Task data:
    input_data = models.JSONField(null=True, blank=True)
    output_data = models.JSONField(null=True, blank=True)

    def __str__(self) -> str:
        return self.pk


    # Meta sub class:
    class Meta:
        app_label = 'automation'