import re

from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def active(request, urls):
    if request.path in ( reverse(url) for url in urls.split() ):
        return 'active'
    return None


@register.simple_tag
def frq(value):
    to_format = float(value)
    formatted = format(float(to_format) / 1000000, '.3f')
    formatted = formatted + ' Mhz'
    return formatted
