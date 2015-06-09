from __future__ import absolute_import

from django.test import TestCase
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime
from django.template import Template, Context
from django import forms

try:
    from bootstrap3 import renderers
except ImportError:
    # nothing to test if we don't have django-bootstrap3 installed
    pass
else:
    from .renderers import BootstrapFieldRenderer

    class RendererTestCase(TestCase):
        def setUp(self):
            class TestForm(forms.Form):
                char = forms.CharField(max_length=255)
                hidden = forms.CharField(max_length=255, widget=forms.HiddenInput())
                date = forms.DateField(widget=AdminDateWidget())
                datetime = forms.DateTimeField(widget=AdminSplitDateTime())

            self.form = TestForm({
                'char': 'hi there',
                'hidden': 'hidden text',
                'date': '20140111',
            })

        def render_template(self, field):
            context = { 'field': field }
            template = Template('{% load bootstrapped_goodies_tags %} {% dab_field_rendering field %}')
            return template.render(Context(context))

        def test_basic_functionality(self):
            field = self.form['char']
            html = self.render_template(field)
            # we prepend this class
            self.assertIn('class="form-control', html)

        def test_hidden_input(self):
            field = self.form['hidden']
            html = self.render_template(field)
            self.assertIn('type="hidden"', html)

        def test_control_inline(self):
            field = self.form['date']
            html = self.render_template(field)
            # we prepend these classes
            self.assertIn('class="form-control form-control-inline', html)

        def test_render_datetime(self):
            field = self.form['datetime']
            html = self.render_template(field)
            self.assertIn('vDateField', html)
            self.assertIn('vTimeField', html)
