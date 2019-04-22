from django import template

from django.contrib.auth.models import User


register = template.Library()

@register.filter
def compact_fullname(user):
    initials = ''
    try:
        for p in user.first_name.split():
            initials += '{}.'.format(p[0].upper())
    except AttributeError:
        return ''
        
    return '{} {}'.format(user.last_name, initials) if initials else user.last_name
