# Django Import:
from django.db import models
from django.utils.translation import gettext_lazy as _

# Applications Import:
from .template import Template
from .automation_policy import AutomationPolicy
from inventory.models.device import Device
from inventory.models.group import Group


# Model code:
class TemplateAutomationPolicyRelation(models.Model):

    # Creation values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    root = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    # Relations values:
    template = models.ForeignKey(Template, on_delete=models.PROTECT)
    automation_policy = models.ForeignKey(AutomationPolicy, on_delete=models.PROTECT)
    sequence = models.IntegerField(unique=True, blank=False)

    class Meta:
        app_label = 'automation'
        unique_together = [['template', 'automation_policy']]


class DeviceAutomationPolicyRelation(models.Model):

    # Creation values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    root = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    # Relations values:
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    automation_policy = models.ForeignKey(AutomationPolicy, on_delete=models.PROTECT)
    sequence = models.IntegerField(unique=True, blank=False)

    class Meta:
        app_label = 'automation'
        unique_together = [['device', 'automation_policy']]


class GroupAutomationPolicyRelation(models.Model):

    # Creation values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    root = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    # Relations values:
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    automation_policy = models.ForeignKey(AutomationPolicy, on_delete=models.PROTECT)
    sequence = models.IntegerField(unique=True, blank=False)

    class Meta:
        app_label = 'automation'
        unique_together = [['group', 'automation_policy']]