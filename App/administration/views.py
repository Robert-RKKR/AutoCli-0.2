# Django Import:
from django.shortcuts import render

# Inventory views:
def login_page(request):
    return render(request, 'administration/login_page.html')