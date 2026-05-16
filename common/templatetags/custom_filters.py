from django import template

register = template.Library()

@register.filter
def repeat(value, times=2):
    return value * times