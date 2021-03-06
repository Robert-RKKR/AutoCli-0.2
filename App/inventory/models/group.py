# Django Import:
from django.db import models
from django.utils.translation import gettext_lazy as _

# Other models Import:
from .device import Device

# Applications Import:
from ..managers import ActiveManager


# Model code:
class Group(models.Model):

    # Creation values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    root = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    # Main model values:
    name = models.CharField(max_length=16, blank=False, unique=True)
    description = models.CharField(max_length=256, default="Group description.")

    # Relationships with other models:
    devices = models.ManyToManyField(Device, through="GroupDeviceRelation")

    # Model representation:
    def __str__(self) -> str:
        return self.name

    # Override default Delete method:
    def delete(self):
        """
            Override the default Delete method to see if the device was created by the Root user,
            if true don't change anything, otherwise change deleted value to true.
        """
        # Check if root value is True:
        if self.root == True:
            # Inform the user that the object cannot be deleted because is a root object:
            assert self.pk is not None, (
                f"{self._meta.object_name} object can't be deleted because its a root object.")
        else:
            # Change deleted value to True, to inform that object is deleted:
            self.deleted = True

    # Meta sub class:
    class Meta:
        app_label = 'inventory'
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')


# Relations models:
class GroupDeviceRelation(models.Model):

    # Creation values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    root = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    # Relations values:
    device = models.ForeignKey(Device, on_delete=models.PROTECT)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)

    class Meta:
        unique_together = [['device', 'group']]