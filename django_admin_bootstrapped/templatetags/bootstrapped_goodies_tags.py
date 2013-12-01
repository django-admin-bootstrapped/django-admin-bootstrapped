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

@register.simple_tag(takes_context=True)
def language_selector(context):
    """ displays a language selector dropdown in the admin, based on Django "LANGUAGES" context.
        requires:
            * USE_I18N = True / settings.py
            * LANGUAGES specified / settings.py (otherwise all Django locales will be displayed)
            * "set_language" url configured (see https://docs.djangoproject.com/en/dev/topics/i18n/translation/#the-set-language-redirect-view)
    """
    output = ""
    from django.conf import settings
    i18 = getattr(settings, 'USE_I18N', False)
    if i18:
        template = "admin/language_selector.html"
        context['i18n_is_set'] = True
        try:
            output = render_to_string(template, context)
        except:
            pass
    return output


@register.filter(name='column_width')
def column_width(value):
    return 12/len(list(value))