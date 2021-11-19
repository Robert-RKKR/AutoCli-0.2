# Django Import:
from unicodedata import name
from django.shortcuts import render

# Inventory views:
def test(request):

    from .models.device import Device
    #new = Device(name="Test", hostname="192.168.1.21")
    #new.save()
    """device = Device.active.get(pk=1)
    print(device)
    print(device.delete())
    device.save()"""

    return render(request, 'inventory/test.html')