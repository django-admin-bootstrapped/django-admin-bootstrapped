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
    return 12 // len(list(value))

@register.filter(name='form_fieldset_column_width')
def form_fieldset_column_width(form):
    def max_line(fieldset):
        return max([len(list(line)) for line in fieldset])

    width = max([max_line(fieldset) for fieldset in form])
    return 12 // width

@register.filter(name='fieldset_column_width')
def fieldset_column_width(fieldset):
    width = max([len(list(line)) for line in fieldset])
    return 12 // width


@register.simple_tag(takes_context=True)
def render_app_name(context, app, fallback="Application name"):
    text = fallback
    try:
        text = app['name']
    except KeyError:
        pass
    except TypeError:
        text = app
    return text


@register.simple_tag(takes_context=True)
def render_app_label(context, app, fallback="Application label"):
    text = fallback
    try:
        text = app['app_label']
    except KeyError:
        pass
    except TypeError:
        text = app
    return text


@register.simple_tag(takes_context=True)
def render_app_description(context, app, template="/admin_app_description.html", fallback="Application description"):
    """ Render the application description using a default template name. If it cannot find a
        template matching the given path, fallback to the application name. If the given
        object is not a dict containing the 'name' key, fallback to the fallback value.
    """
    text = fallback
    try:
        try:
            template = app['app_label'] + template
            text = render_to_string(template, context)
        except:
            text = app['name']
    except:
        pass
    return text
