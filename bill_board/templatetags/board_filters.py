from django import template

register = template.Library()


@register.filter()
def attach_name(in_text):
    # Truncate path from file name
    return str(in_text).split('/')[-1]
