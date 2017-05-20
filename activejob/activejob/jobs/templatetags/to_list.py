
""" custom filter for job descriptions"""
from django import template

register = template.Library()

@register.filter
def to_list(value):
    list = value.split("- ")
    del list[0]
    return list
