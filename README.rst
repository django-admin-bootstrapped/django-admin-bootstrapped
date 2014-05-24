django-admin-bootstrapped
=========================

|PyPI version|

A Django admin theme using Twitter Bootstrap. It doesn't need any kind
of modification on your side, just add it to the installed apps.

Requirements
------------

-  Django ``>=1.4.x``.

Installation
------------

1. Download it from PyPi with ``pip install django-admin-bootstrapped``
2. Add ``'django_admin_bootstrapped'`` into the ``INSTALLED_APPS`` list
   **before** ``'django.contrib.admin'``
3. Have fun!

Switch to Bootstrap3
~~~~~~~~~~~~~~~~~~~~

Do the previous steps, then add
``'django_admin_bootstrapped.bootstrap3'`` into the ``INSTALLED_APPS``
list **before** ``'django_admin_bootstrapped'``.

Goodies
-------

Translate/change an application name with a template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With the default admin you can't change the application name, but
django-admin-bootstrapped let you do it in a really easy way. Just
create a file named ``admin_app_name.html`` into the application's
template folder. Eg: ``myapp/templates/admin_app_name.html`` or
``project/templates/myapp/admin_app_name.html``. You can also change the
default Django Administration title, just add a ``admin_title.html``
file into your ``project/templates/admin/`` folder.

Add custom html to the change form of any model with a template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can inject custom html on top of any change form creating a template
named ``admin_model_MODELNAME_change_form.html`` into the application's
template folder. Eg:
``myapp/templates/myapp/admin_model_mymodelname_change_form.html`` or
``project/templates/myapp/admin_model_mymodelname_change_form.html``.

Inline sortable
~~~~~~~~~~~~~~~

You can add drag&drop sorting capability to any inline with a couple of
changes to your code.

First, add a ``position`` field in your model (and sort your model
accordingly), for example:

::

    class TestSortable(models.Model):
        that = models.ForeignKey(TestMe)
        position = models.PositiveSmallIntegerField("Position")
        test_char = models.CharField(max_length=5)

        class Meta:
            ordering = ('position', )

Then in your admin.py create a class to handle the inline using the
``django_admin_bootstrapped.admin.models.SortableInline`` mixin, like
this:

::

    from django_admin_bootstrapped.admin.models import SortableInline
    from models import TestSortable

    class TestSortable(admin.StackedInline, SortableInline):
        model = TestSortable
        extra = 0

You can now use the inline as usual. The result will look like this:

This feature was brought to you by `Kyle
Bock <https://github.com/kwbock>`__. Thank you Kyle!

XHTML Compatible
~~~~~~~~~~~~~~~~

Compatible with both html and xhtml. To enable xhtml for your django app
add the following to your settings.py: DEFAULT\_CONTENT\_TYPE =
'application/xhtml+xml'

Generic lookups in admin
~~~~~~~~~~~~~~~~~~~~~~~~

All that needs to be done is change the admin widget with either
formfield\_overrides like this:

::

    from django_admin_bootstrapped.widgets import GenericContentTypeSelect

    class SomeModelAdmin(admin.ModelAdmin):
        formfield_overrides = {
            models.ForeignKey: {'widget': GenericContentTypeSelect},
        }

Or if you want to be more specific:

::

    from django_admin_bootstrapped.widgets import GenericContentTypeSelect

    class SomeModelAdmin(admin.ModelAdmin):
        def formfield_for_dbfield(self, db_field, **kwargs):
            if db_field.name == 'content_type':
                kwargs['widget'] = GenericContentTypeSelect
            return super(SomeModelAdmin, self).formfield_for_dbfield(db_field, **kwargs)

If you decide on using ``formfield_overrides`` `you should be aware of
its limitations with relation
fields <https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.formfield_overrides>`__.

This feature (and many more) was brought to you by `Jacob
Magnusson <https://github.com/jmagnusson>`__. Thank you Jacob!

Screenshots
-----------

Homepage
~~~~~~~~

List view with filters in dropdown
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Change form view
~~~~~~~~~~~~~~~~

.. |PyPI version| image:: https://pypip.in/d/django-admin-bootstrapped/badge.png
   :target: https://pypi.python.org/pypi/django-admin-bootstrapped
