# Django Import:
from django.shortcuts import render

# Inventory views:
def login_page(request):
    return render(request, 'administration/login_page.html')

# Inventory views:
def dashboard(request):
    return render(request, 'administration/dashboard.html')