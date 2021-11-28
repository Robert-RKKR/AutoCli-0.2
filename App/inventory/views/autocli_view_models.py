# Django Imports:
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

# Class:
class AutoCliBaseViewModel(View):

    # Class attributes:
    template = None
    page_name = None
    panel = None
    filter = None
    messages = []
    application = None
    model = None

    def print_page_name(self):
        """ Return page name created base on add text and model name. """

        # Check if page name is provided, if not return newone:
        if self.page_name is None:
            text = _('Add new')
            model_name = str(self.model._meta.verbose_name)
            return text + ' ' + model_name
        else:
            return self.page_name

    """def get(self, request, *args, **kwargs):

        return render(request, self.template, {
            'page_name': self.print_page_name(),
            'panel': self.panel,
            'filter': self.filter,
            'messages': self.messages,
            'application': self.application,
            'model': self.model,
        })"""


class AddViewModel(AutoCliBaseViewModel):

    # Class attributes:
    form_class = None

    def get(self, request, *args, **kwargs):
        url = request.path[3:]

        # Use provided form:
        form = self.form_class

        return render(request, self.template, {
            'page_name': self.print_page_name(),
            'panel': self.panel,
            'filter': self.filter,
            'messages': self.messages,
            'application': self.application,
            'model': self.model,
            'form': form,
            'url': url,
        })
    
    def post(self, request, *args, **kwargs):
        url = request.path[3:]
        
        # Use provided form:
        form = self.form_class(request.POST)

        # Clear messages:
        self.messages = []

        # Check if form is valid:
        if form.is_valid():
            new_object = form.save()

            # Create and display message:
            message = {}
            message['message_text'] = new_object.name + ' ' + _('was added to database.')
            message['message_type'] = _('INFORM')
            message['message_ico'] = 'inform'
            self.messages.append(message)

        return render(request, self.template, {
            'page_name': self.print_page_name(),
            'panel': self.panel,
            'filter': self.filter,
            'messages': self.messages,
            'application': self.application,
            'model': self.model,
            'form': form,
            'url': url,
        })