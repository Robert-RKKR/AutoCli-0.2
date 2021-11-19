# Django Import:
from django.shortcuts import render

# Forms Import:
from ..forms import DeviceAddOneForm

# Application Import:
from ..models.device import Device

# Inventory views:
def device_add_one(request):
    
    data = {
        'form': DeviceAddOneForm(),
        'model_name': Device._meta.object_name,
    }

    if request.method == 'POST':
        form = DeviceAddOneForm(request.POST)
        data['form'] = form

        if form.is_valid:
            form.save()
    
    elif request.method == 'GET':
        pass

    return render(request, 'inventory/add_form.html', data)