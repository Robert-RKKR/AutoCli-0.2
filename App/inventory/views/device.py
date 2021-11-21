# Django Import:
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

# Forms Import:
from ..forms import DeviceAddOneForm

# Application Import:
from ..models.device import Device

# Application Filters Import:
from ..filters import DeviceFilter, DeviceNameFilter


# Device panel:
main_path = '/inventory/device'
panel = {
    'link': {
        'application': 'inventory',
        'model': 'device',
    },
    'views': ['grid', 'list'],
    'actions': [
        'add', 'edit', 'delete',
    ],
}


# Inventory views:
def add(request):

    # Collect basic information:
    data = {
        'url': request.path[3:],
        'page_name': _('Add new device'),
        'messages': [],
        'panel': panel,
    }

    # Show form if GET and form output when POST:
    if request.method == 'POST':
        form = DeviceAddOneForm(request.POST)
        data['form'] = form

        # Try to add a nwe object if form is valid:
        if form.is_valid():
            message = {} # New message dict.
            new_device = form.save() 
            message['message_text'] = new_device.name + ' ' + _('was added to database.')
            message['message_type'] = _('INFORM')
            message['message_ico'] = 'inform'
            data['messages'].append(message)
        
        return render(request, 'inventory/add_form.html', data)
    
    elif request.method == 'GET':
     
        data['form'] = DeviceAddOneForm()

        return render(request, 'inventory/add_form.html', data)


def search(request):

    # Collect basic information:
    data = {
        'url': request.path[3:],
        'page_name': _('All devices search'),
        'messages': [],
        'panel': panel,
        'main_path': main_path,
    }

    # Collect name:
    object_name = request.GET.get('object_name')
    
    if object_name == '':
        # Collect devices:
        devices = Device.objects.all()

        # Filter:
        devices_filter = DeviceFilter(request.GET, queryset=devices)
        data['objects'] = devices_filter.qs
        data['filter'] = devices_filter

    else:
        # Collect all devices:
        devices = Device.objects.filter(name__contains=object_name)
    
        # Filter:
        devices_filter = DeviceFilter(request.GET, queryset=devices)
        data['objects'] = devices_filter.qs
        data['filter'] = devices_filter

    return render(request, 'inventory/search.html', data)
