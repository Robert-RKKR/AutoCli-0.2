# Django Import:
from django.shortcuts import render

# Inventory views:
def test(request):
    return render(request, 'inventory/test.html')