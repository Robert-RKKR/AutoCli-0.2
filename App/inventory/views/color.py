# Django Imports:
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _

# Application Import:
from ..models.color import Color

# Application Filters Import:
from ..filters import ColorFilter

# Application Forms Import:
from ..forms import ColorForm

# Model web data:
data = {
    'application': 'inventory',
    'model': 'color',
    'panel': '',
}
