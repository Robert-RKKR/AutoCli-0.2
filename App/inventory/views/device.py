# Django Import:
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

# Forms Import:
from ..forms import DeviceAddOneForm

# Application Import:
from ..models.device import Device

# Inventory views:
def device_add_one(request):

    # Collect basic information:
    data = {
        'url': request.path[3:],
        'model_name': Device._meta.object_name,
        'messages': [],
    }

    # Show form if GET and form output when POST:
    if request.method == 'POST':
        form = DeviceAddOneForm(request.POST)
        data['form'] = form

        # Try to add a nwe object if form is valid:
        if form.is_valid():
            message = {} # New message dict.
            new_device = form.save() 
            message['message_text'] = new_device.name + ' ' + _('Was added to database.')
            message['message_type'] = _('INFORM')
            data['messages'].append(message)
        
        return render(request, 'inventory/add_form.html', data)
    
    elif request.method == 'GET':
     
        data['form'] = DeviceAddOneForm()

        return render(request, 'inventory/add_form.html', data)