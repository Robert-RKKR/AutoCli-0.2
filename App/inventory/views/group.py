# Application Import:
from .autocli_view_models import *
from ..models.group import Group

# Application Filters Import:
from ..filters import GroupFilter

# Application Forms Import:
from ..forms import GroupForm


class GroupOneView(OneViewModel):

    model = Group
    panel = ['add', 'update', 'delete']
    display = ['description', 'devices']


class GroupAddView(AddViewModel):

    model = Group
    form_class = GroupForm
    panel = ['add']


class GroupDeleteView(DeleteViewModel):

    model = Group
    form_class = GroupForm
    panel = ['add']


class GroupUpdateView(UpdateViewModel):

    model = Group
    form_class = GroupForm
    panel = ['add', 'delete']


class GroupSearchView(SearchViewModel):

    model = Group
    filter = GroupFilter
    panel = ['add']
    display = ['description']
