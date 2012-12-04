from django import template
from django.template.loader import render_to_string, TemplateDoesNotExist

register = template.Library()


@register.simple_tag(takes_context=True)
def render_with_template_if_exist(context, template, fallback):
    text = fallback
    try:
        text = render_to_string(template, context)
    except:
        pass
    return text
