# Django Imports:
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.views.generic import View
from prompt_toolkit import application

# Application Import:
from .autocli_view_models import AddViewModel
from ..models.color import Color

# Application Filters Import:
from ..filters import ColorFilter

# Application Forms Import:
from ..forms import ColorForm

# Model web data:
data_view = {
    'application': 'inventory',
    'model': 'color',
    'panel': '',
}

class ColorAddView(AddViewModel):

    template = 'add_object.html'
    application = 'inventory'
    model = Color
    form_class = ColorForm

