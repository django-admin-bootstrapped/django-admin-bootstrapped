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

@register.inclusion_tag('admin/language_selector.html', takes_context=True)
def language_selector(context):
    from django.conf import settings
    i18 = getattr(settings, 'USE_I18N', False)
    if i18:
        context['i18n_is_set'] = True
    return context
