# Django Imports:
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, get_object_or_404

# Application Import:
from ..tasks import single_device_check

def test(request):
    data = {
        'output': 'RKKR'
    }

    data['output'] = single_device_check(52)
    #data['output'] = single_device_check.delay(52)

    return render(request, 'test.html', data)