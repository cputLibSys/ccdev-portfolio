from django import template

register = template.Library()

@register.filter
def get_el(obj, attr):

    return getattr(obj, attr)

@register.filter('split')
def split(data, key):

    return data.split(key)

