django-admin-bootstrapped
=========================

A Django admin theme using Twitter Bootstrap. It doesn't need any kind of modification on your side, just add it to the installed apps.

## Screenshots

<img src="http://www.codingnot.es/static/screens/django_admin_bootstrapped_screen_0.png">
<img src="http://www.codingnot.es/static/screens/django_admin_bootstrapped_screen_1.png">
<img src="http://www.codingnot.es/static/screens/django_admin_bootstrapped_screen_2.png">

## Requirements

* Django `1.4.x`.

## Installation

1. Download it from PyPi with `pip install django-admin-bootstrapped`
2. Add `'django_admin_bootstrapped'` into the `INSTALLED_APPS` list __before__ `'django.contrib.admin'`
3. Have fun!

## Goodies

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

