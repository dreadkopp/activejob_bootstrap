
""" custom filter for urls in page TextField"""
from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.filter
def get_url(text):
    #TODO: search text for {% url 'foo' %}, replace with reverse('foo')
    
    return text
