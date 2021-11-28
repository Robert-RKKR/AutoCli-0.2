# Django Imports:
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.views.generic import View
from prompt_toolkit import application

# Application Import:
from .autocli_view_models import *
from ..models.color import Color

# Application Filters Import:
from ..filters import ColorFilter

# Application Forms Import:
from ..forms import ColorForm


class ColorOneView(OneViewModel):

    model = Color
    panel = ['add', 'update', 'delete']
    display = ['value', 'description', 'devices', 'groups', 'credentials']


class ColorAddView(AddViewModel):

    model = Color
    form_class = ColorForm
    panel = ['add']


class ColorDeleteView(DeleteViewModel):

    model = Color
    form_class = ColorForm
    panel = ['add']


class ColorUpdateView(UpdateViewModel):

    model = Color
    form_class = ColorForm
    panel = ['add', 'delete']


class ColorSearchView(SearchViewModel):

    model = Color
    filter = ColorFilter
    panel = ['add']
    display = ['value']
