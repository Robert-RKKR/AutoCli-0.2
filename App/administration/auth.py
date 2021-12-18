# Django Imports:
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect, render

# Form Import:
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


class AuthRequiredMiddleware(object):
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        if not request.user.is_authenticated:
            data = {}

            # Collect user data:
            if request.method == "POST":
                data['form'] = UserCreationForm()
                username = request.POST.get('username')
                password = request.POST.get('password')

                # Authenticate user:
                user = authenticate(request, username=username, password=password)

                # Login user:
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
            
            return render(request, 'administration/login_page.html', data)
        
        # Code to be executed for each request/response after
        # the view is called.

        return response
