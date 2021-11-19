# Django Import:
from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible
from django.core import validators


# Validators class:
@deconstructible
class ColorValueValidator(validators.RegexValidator):
    regex = r'^#([0-9,A-F,a-f]{3}|[0-9,A-F,a-f]{6})$'
    message = _(
        'Enter the correct colour in hexadecimal notation. This value can only contain hexadecimal numbers preceded by the # sign.'
    )
    flags = 0