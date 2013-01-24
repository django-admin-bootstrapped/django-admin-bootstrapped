django-admin-bootstrapped
=========================

A Django admin theme using Twitter Bootstrap. It doesn't need any kind of modification on your side, just add it to the installed apps.

## Requirements

* Django `1.4.x`.

## Installation

1. Download it from PyPi with `pip install django-admin-bootstrapped`
2. Add `'django_admin_bootstrapped'` into the `INSTALLED_APPS` list __before__ `'django.contrib.admin'`
3. Have fun!

## Goodies

### Translate/change an application name with a template

With the default admin you can't change the application name, but django-admin-bootstrapped let you do it in a really easy way. Just create a file named `admin_app_name.html` into the application's template folder. Eg: `myapp/templates/admin_app_name.html` or `project/templates/myapp/admin_app_name.html`.

### Add custom html to the change form of any model with a template

You can inject custom html on top of any change form creating a template named `admin_model_MODELNAME_change_form.html` into the application's template folder. Eg: `myapp/templates/admin_model_mymodelname_change_form.html` or `project/templates/myapp/admin_model_mymodelname_change_form.html`.

### Inline sortable

You can add drag&drop sorting capability to any inline with a couple of changes to your code.

First, add a `position` field in your model (and sort your model accordingly), for example:

    class TestSortable(models.Model):
        that = models.ForeignKey(TestMe)
        position = models.PositiveSmallIntegerField("Position")
        test_char = models.CharField(max_length=5)

        class Meta:
            ordering = ('position', )

Then in your admin.py create a class to handle the inline using the `django_admin_bootstrapped.admin.models.SortableInline` mixin, like this:

    from django_admin_bootstrapped.admin.models import SortableInline
    from models import TestSortable

    class TestSortable(admin.StackedInline, SortableInline):
        model = TestSortable
        extra = 0

You can now use the inline as usual. The result will look like this:

<img src="http://www.codingnot.es/static/screens/django_admin_bootstrapped_screen_inlines.png">

This feature was brought to you by [Kyle Bock](https://github.com/kwbock). Thank you Kyle!

## Screenshots

### Homepage

<img src="http://www.codingnot.es/static/screens/django_admin_bootstrapped_screen_v02_index.png">

### List view with filters in dropdown

<img src="http://www.codingnot.es/static/screens/django_admin_bootstrapped_screen_v02_list_filter.png">

### Change form view

<img src="http://www.codingnot.es/static/screens/django_admin_bootstrapped_screen_v02_change_form.png">
