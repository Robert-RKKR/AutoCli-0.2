# Django Imports:
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

# Class:

class AutoCliBaseViewModel(View):
    """
        Base AutoCli View Model, contains basic attributes and methods used by other View Models.
    """

    # Class attributes:
    template = None
    page_name = None
    panel = None
    filter = None
    messages = []
    model = None
    display = None
    model_view_url = None
    page_data = {}
    grid = True
    edit = None

    def get(self, request, *args, **kwargs):

        # Clear messages:
        type(self).messages = []

        # Model name:
        type(self).model_view_url = str(type(self).model.__name__).lower

        # Default return data:
        type(self).page_data = {
            'page_name': self.get_page_name(),
            'panel': type(self).panel,
            'filter': type(self).filter,
            'messages': type(self).messages,
            'model': type(self).model,
            'display': type(self).display,
            'model_view_url': type(self).model_view_url,
            'grid': type(self).grid,
            'edit': type(self).edit,
        }

    def post(self, request, *args, **kwargs):

        # Clear messages:
        type(self).messages = []

        # Model name:
        type(self).model_view_url = str(type(self).model.__name__).lower

        # Default return data:
        type(self).page_data = {
            'page_name': self.get_page_name(),
            'panel': type(self).panel,
            'filter': type(self).filter,
            'messages': type(self).messages,
            'model': type(self).model,
            'display': type(self).display,
            'model_view_url': type(self).model_view_url,
        }

    def get_page_name(self, text_to_display=None):
        """ Return given page name if provided, or created newone base on added text and model name. """

        # Check if page name is provided, if not return newone:
        if self.page_name is None:
            model_name = str(self.model._meta.verbose_name)
            if text_to_display is None:
                return model_name
            else:
                return text_to_display + ' ' + model_name
        else:
            return self.page_name

    def get_attribute(self, attribute, default):
        """ Return given attribute if provided or default one. """

        # Value to return:
        output_template = None

        # Check if given attribute is provided, if not return newone:
        if attribute is None: 
            output_template = default
        else:
            output_template = attribute

        # Return value:
        return output_template


class AddViewModel(AutoCliBaseViewModel):
    """
        Add View Model, takes form_class attributes contains valid django form and display form on page.
    """

    # Class attributes:
    form_class = None

    # Static class attributes:
    display_text = _('Add new')

    def get(self, request, *args, **kwargs):
        super().get(request)

        # Use provided form:
        type(self).page_data['form'] = type(self).form_class

        # Use default add page name:
        type(self).page_data['page_name'] = self.get_page_name(type(self).display_text)

        # Return valid page with provided or default data:
        return render(request, self.get_attribute(type(self).template, 'add_object.html'), self.page_data)
        
    
    def post(self, request, *args, **kwargs):
        super().post(request)
        
        # Use provided form:
        form = type(self).form_class(request.POST)
        type(self).page_data['form'] = form

        # Use default add page name:
        type(self).page_data['page_name'] = self.get_page_name(type(self).display_text)

        # Check if form is valid:
        if form.is_valid():
            new_object = form.save()
            # Create and display message:
            message = {}
            message['message_text'] = new_object.name + _(' was added to database.')
            message['message_type'] = _('INFORM')
            message['message_ico'] = 'inform'
            type(self).page_data['messages'].append(message)

        # Return valid page with provided or default data:
        return render(request, self.get_attribute(type(self).template, 'add_object.html'), self.page_data)


class SearchViewModel(AutoCliBaseViewModel):
    """
        Search View Model, return all objects page with search bar.
    """

    # Class attributes:
    form_class = None

    # Static class attributes:
    display_text = _('Search')

    def get(self, request, *args, **kwargs):
        super().get(request)

        # Add edit option to panel:
        type(self).edit = True

        # Collect data from name form field:
        object_name = request.GET.get('object_name')

        if object_name == '' or object_name is None:

            # Collect objects:
            collected_objects = type(self).model.objects.all()

            # Use filters:
            objects_filter = type(self).filter(request.GET, queryset=collected_objects)
            type(self).page_data['objects'] = objects_filter.qs
            type(self).page_data['filter'] = objects_filter

        else:

            # Collect filtered objects:
            collected_filtered_objects = type(self).model.objects.filter(name__icontains=object_name)
            
            # Use filters:
            objects_filter = type(self).filter(request.GET, queryset=collected_filtered_objects)
            type(self).page_data['objects'] = objects_filter.qs
            type(self).page_data['filter'] = objects_filter

        # Use default add page name:
        type(self).page_data['page_name'] = self.get_page_name(type(self).display_text)

        # Return valid page with provided or default data:
        return render(request, self.get_attribute(type(self).template, 'search.html'), self.page_data)


class OneViewModel(AutoCliBaseViewModel):
    """
        One object View Model, takes pk of object to display details information's about object.
    """

    # Class attributes:
    form_class = None

    # Static class attributes:
    display_text = _('One')

    def get(self, request, *args, **kwargs):
        super().get(request)

        # Collect object:
        collected_object = get_object_or_404(type(self).model, pk=kwargs['pk'])
        type(self).page_data['object'] = collected_object
        type(self).page_data['object_pk'] = kwargs['pk']

        # Use default add page name:
        type(self).page_data['page_name'] = self.get_page_name(type(self).display_text)

        # Return valid page with provided or default data:
        return render(request, self.get_attribute(type(self).template, 'one_object.html'), self.page_data)


class UpdateViewModel(AutoCliBaseViewModel):
    """
        Update View Model, takes form_class attributes contains valid django form and display edit form on page.
    """

    # Class attributes:
    form_class = None

    # Static class attributes:
    display_text = _('Add new')

    def get(self, request, *args, **kwargs):
        super().get(request)

        # Collect object:
        collected_object = get_object_or_404(type(self).model, pk=kwargs['pk'])
        type(self).page_data['object_pk'] = kwargs['pk']

        # Use provided form:
        type(self).page_data['form'] = type(self).form_class(instance=collected_object)

        # Use default add page name:
        type(self).page_data['page_name'] = self.get_page_name(type(self).display_text)

        # Return valid page with provided or default data:
        return render(request, self.get_attribute(type(self).template, 'add_object.html'), self.page_data)
        
    
    def post(self, request, *args, **kwargs):
        super().post(request)

        # Collect object:
        collected_object = get_object_or_404(type(self).model, pk=kwargs['pk'])
        type(self).page_data['object_pk'] = kwargs['pk']
        
        # Use provided form:
        form = type(self).form_class(request.POST, instance=collected_object)
        type(self).page_data['form'] = form

        # Use default add page name:
        type(self).page_data['page_name'] = self.get_page_name(type(self).display_text)

        # Check if form is valid:
        if form.is_valid():
            updated_object = form.save()
            # Create and display message:
            message = {}
            message['message_text'] = updated_object.name +  _(' was edited.')
            message['message_type'] = _('INFORM')
            message['message_ico'] = 'inform'
            type(self).page_data['messages'].append(message)

        # Return valid page with provided or default data:
        return render(request, self.get_attribute(type(self).template, 'add_object.html'), self.page_data)


class DeleteViewModel(AutoCliBaseViewModel):
    """
        Delete View Model, deletes object from database.
    """

    # Class attributes:
    form_class = None

    # Static class attributes:
    display_text = _('One')

    def get(self, request, *args, **kwargs):
        super().get(request)

        # Collect object:
        collected_object = get_object_or_404(type(self).model, pk=kwargs['pk'])
        object_name = collected_object.name
        collected_object.delete()

        # Create and display message:
        message = {}
        message['message_text'] = object_name +  _(' was deleted.')
        message['message_type'] = _('INFORM')
        message['message_ico'] = 'error'
        type(self).page_data['messages'].append(message)

        # Use default add page name:
        type(self).page_data['page_name'] = self.get_page_name(object_name)

        # Return valid page with provided or default data:
        return render(request, self.get_attribute(type(self).template, 'message.html'), self.page_data)
