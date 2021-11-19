# Django Import:
from django.db import models
from django.utils.translation import gettext_lazy as _

# Applications Import:
from ..managers import NotDeleted, ActiveManager
from .icons import ICONS

# Other models Import:
from .credential import Credential


# Model code:
class Device(models.Model):

    # Static values:
    STATUS_CHOICES = (
        (0, _('Nonactive')),
        (1, _('Active')),
    )
    DEVICE_TYPE = (
        (0, _('autodetect')),
        (1, _('cisco_ios')),
        (2, _('cisco_xr')),
        (3, _('cisco_xe')),
        (4, _('cisco_nxos')),
    )

    # Creation values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    root = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    # Device status:
    ssh_status = models.BooleanField(default=False)
    https_status = models.BooleanField(default=False)

    # Main model values:
    name = models.CharField(max_length=16, blank=False, unique=True)
    hostname = models.CharField(
        max_length=64,
        blank=False,
        unique=True,
        error_messages={
            'null': _('This field is mandatory.'),
            'blank': _('This field is mandatory.'),
            'unique': _('This field must be unique.'),
        },
        help_text=_('Enter a valid IP address or DNS resolvable hostname.'),
    )
    device_type = models.IntegerField(choices=DEVICE_TYPE, default=0)
    ico = models.IntegerField(choices=ICONS, default=0)
    ssh_port = models.IntegerField(default=22)
    https_port = models.IntegerField(default=443)
    description = models.CharField(max_length=256, default="Device description.")

    # Security and credentials:
    credential = models.ForeignKey(Credential, on_delete=models.PROTECT, null=True, blank=True)
    secret = models.CharField(max_length=64, null=True, blank=True)
    token = models.CharField(max_length=128, null=True, blank=True)
    certificate = models.BooleanField(default=False)

    # Object managers:
    objects = NotDeleted()
    active = ActiveManager()

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
