# Django Import:
from django import template

# Register template:
register = template.Library()

# Filters:
@register.filter
def verbose_name(template_object):
    return template_object._meta.verbose_name

@register.filter
def verbose_name_plural(template_object):
    return template_object._meta.verbose_name_plural

@register.filter
def key_value(template_object, key):
    return getattr(template_object, key)

@register.filter
def language_url(request):
    return request.path[3:]

@register.filter
def create_url(action, text):
    return text + '_' + action
