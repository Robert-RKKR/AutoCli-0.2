# Django Import:
from django.db import models
from django.utils.translation import gettext_lazy as _

# Other models Import:
from .credential import Credential
from .device import Device
from .group import Group

# Validators Import:
from ..validators import ColorValueValidator

# Applications Import:
from ..managers import NotDeleted

# Model code:
class Color(models.Model):
    """ Color model is working like Tag, available to be added to all device, group and credential models. """

    # Validators:
    color_validator = ColorValueValidator()

    # Creation values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    root = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    # Main model values:
    name = models.CharField(max_length=32, blank=False, unique=True)
    value = models.CharField(
        unique=True,
        max_length=7,
        validators=[color_validator],
        help_text=_('Hexadecimal representation of colour, for example #73a6ff.'),
        error_messages={
            'null': _('This field is mandatory.'),
            'blank': _('This field is mandatory.'),
            'invalid': _('Enter the correct colour value. It must be a 3/6 hexadecimal number with # character on begining'),
        },
    )
    description = models.CharField(max_length=256, default="Color description.")

    # Relationships with other models:
    devices = models.ManyToManyField(Device, through="ColorDeviceRelation")
    groups = models.ManyToManyField(Group, through="ColorGroupRelation")
    credentials = models.ManyToManyField(Credential, through="ColorCredentialRelation")

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

    # Object managers:
    objects = NotDeleted()

    # Meta sub class:
    class Meta:
        app_label = 'inventory'



# Relations models:
class ColorDeviceRelation(models.Model):

    # Creation values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    root = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    # Relations values:
    device = models.ForeignKey(Device, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)

    class Meta:
        unique_together = [['device', 'color']]


class ColorGroupRelation(models.Model):

    # Creation values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    root = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    # Relations values:
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)

    class Meta:
        unique_together = [['group', 'color']]


class ColorCredentialRelation(models.Model):

    # Creation values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    root = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    # Relations values:
    credential = models.ForeignKey(Credential, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)

    class Meta:
        unique_together = [['credential', 'color']]
