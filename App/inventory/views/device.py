# Django Import:
from django.shortcuts import render, get_object_or_404
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
}


# Inventory views:
def add(request):

    # Collect basic information:
    panel['actions'] = [{'name': 'add'}]
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
        
        return render(request, 'add_form.html', data)
    
    elif request.method == 'GET':
     
        data['form'] = DeviceAddOneForm()

        return render(request, 'add_form.html', data)

def one(request, pk):
    # Collect basic information:
    data = {
        'url': request.path[3:],
        'messages': [],
        'panel': panel,
    }

    device = get_object_or_404(Device, pk=pk)
    panel['actions'] = [
        {
            'name': 'add',
        },
        {
            'name': 'edit',
            'object': pk,},
        {
            'name': 'delete',
            'object': pk,},
    ]
    data['page_name'] = device.name
    data['object'] = device

    return render(request, 'inventory/one.html', data)

def edit(request, pk):
    # Collect basic information:

    panel['actions'] = [
        {
            'name': 'add',
        },
        {
            'name': 'edit',
            'object': pk,},
        {
            'name': 'delete',
            'object': pk,},
    ]
    data = {
        'url': request.path[3:],
        'page_name': _('Edit device'),
        'messages': [],
        'panel': panel,
    }

    # Collect devices:
    device = get_object_or_404(Device, pk=pk)

    # Show form if GET and form output when POST:
    if request.method == 'POST':
        form = DeviceAddOneForm(request.POST, instance=device)
        data['form'] = form

        # Try to add a nwe object if form is valid:
        if form.is_valid():
            message = {} # New message dict.
            new_device = form.save() 
            message['message_text'] = new_device.name + ' ' + _('object was edited.')
            message['message_type'] = _('INFORM')
            message['message_ico'] = 'inform'
            data['messages'].append(message)
        
        return render(request, 'add_form.html', data)
    
    elif request.method == 'GET':
     
        data['form'] = DeviceAddOneForm(instance=device)

    return render(request, 'add_form.html', data)

def search(request):

    # Collect basic information:
    panel['actions'] = [{'name': 'add'}]
    data = {
        'url': request.path[3:],
        'page_name': _('Devices search'),
        'messages': [],
        'panel': panel,
        'main_path': main_path,
        'display': [
            'hostname', 'device_type', 'credential', 'ssh_port', 'https_port', 
        ]
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
