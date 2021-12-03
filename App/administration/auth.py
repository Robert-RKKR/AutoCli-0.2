# Django Imports:
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render


class AuthRequiredMiddleware(object):
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        if not request.user.is_authenticated: # in Django > 3 this is a boolean
            return render(request, 'administration/login_page.html')
        
        # Code to be executed for each request/response after
        # the view is called.

        return response
