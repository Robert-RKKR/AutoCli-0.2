# Application Import:
from main.autocli_view_models import *
from ..models.credential import Credential

# Application Filters Import:
from ..filters import CredentialFilter

# Application Forms Import:
from ..forms import CredentialForm


class CredentialOneView(OneViewModel):

    model = Credential
    panel = ['add', 'update', 'delete']
    display = ['username', 'password', 'description']


class CredentialAddView(AddViewModel):

    model = Credential
    form_class = CredentialForm
    panel = ['add']


class CredentialDeleteView(DeleteViewModel):

    model = Credential
    form_class = CredentialForm
    panel = ['add']


class CredentialUpdateView(UpdateViewModel):

    model = Credential
    form_class = CredentialForm
    panel = ['add', 'delete']


class CredentialSearchView(SearchViewModel):

    model = Credential
    filter = CredentialFilter
    panel = ['add']
    display = ['username', 'password']
