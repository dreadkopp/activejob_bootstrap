from django import template
from django.template import loader
from django.template import engines

register = template.Library()

@register.filter
def render_from_string(text):
    django_engine = engines['django']
    template = django_engine.from_string(text)
    text = template.render()
    return text
