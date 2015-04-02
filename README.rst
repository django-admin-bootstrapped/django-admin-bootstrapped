django-admin-bootstrapped
=========================

|PyPI version|

A Django admin theme using Bootstrap. It doesn't need any kind
of modification on your side, just add it to the installed apps.

Requirements
------------

-  Django ``==1.7``

Django 1.6 has been supported up to the ``2.3.x`` series

Django 1.7 will be supported up to the ``2.4.x`` series

Installation
------------

1. Download it from PyPi with ``pip install django-admin-bootstrapped``
2. Add into the ``INSTALLED_APPS`` **before** ``'django.contrib.admin'``:

::

    'django_admin_bootstrapped',

3. Have fun!

Configuration
-------------

For a full bootstrap3 experience you may want to use a custom renderer for the fields.
There's one available in tree that requires the ``django-bootstrap3`` application installed.
You have to add to your project settings file:
::

    DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'


`Messages <http://docs.djangoproject.com/en/dev/ref/contrib/messages>`__ will have ``alert-info`` tag by default, 
so you may want to add Bootstrap 3 tags for different message levels to make them styled appropriately.
Add to your project settings file:
::

    from django.contrib import messages
    
    MESSAGE_TAGS = {
                messages.SUCCESS: 'alert-success success',
                messages.WARNING: 'alert-warning warning',
                messages.ERROR: 'alert-danger error'
    }

Now, adding messages like this:
::

    messages.success(request, "My success message")
    messages.warning(request, "My warning message")
    messages.error(request, "My error message")

will result into this:

.. image:: https://i.imgur.com/SQNMZZE.png

Goodies
-------

Translate/change an application name with a template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**This will be removed in 2.5.0**

With a version of django ``< 1.7`` you can't change the application
name, but django-admin-bootstrapped let you do it in a really easy way.
Create a file named ``admin_app_name.html`` into the application's
template folder. Eg: ``myapp/templates/admin_app_name.html`` or
``project/templates/myapp/admin_app_name.html``.

You can also change the default Django Administration title, just add a
``admin_title.html`` file into your ``project/templates/admin/`` folder.

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

You can now use the inline as usual. See the screenshots section to see what the result
will look like.

This feature was brought to you by `Kyle Bock <https://github.com/kwbock>`__. Thank you Kyle!


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

Contributing
------------

Every code, documentation and UX contribution is welcome.

Found an issue? Report it in the bugtracker!

Have some free time? Help fixing an already filed issue, just remember to work on a separate branch please.

Screenshots
-----------

Homepage
~~~~~~~~

.. image:: https://cloud.githubusercontent.com/assets/12932/6967318/d7064abe-d95e-11e4-91bc-6de527550557.png

List view with filters in dropdown
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://cloud.githubusercontent.com/assets/12932/6967319/d71a9c6c-d95e-11e4-86cf-47e8857582c1.png

Change form view
~~~~~~~~~~~~~~~~

.. image:: https://cloud.githubusercontent.com/assets/12932/6966950/98661ba6-d95c-11e4-8bb3-e4b18759115b.png

.. |PyPI version| image:: https://pypip.in/d/django-admin-bootstrapped/badge.png
   :target: https://pypi.python.org/pypi/django-admin-bootstrapped
