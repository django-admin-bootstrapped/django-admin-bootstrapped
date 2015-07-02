from django.forms.widgets import CheckboxSelectMultiple
from django.contrib import admin
from django.db import models

from django_admin_bootstrapped.admin.models import SortableInline

from .models import TestMe, TestThat, TestMeProxyForFieldsets, TestSortable


class TestThatStackedInline(admin.StackedInline):
    model = TestThat

class TestThatStackedFieldsetInline(admin.StackedInline):
    model = TestThat
    fieldsets = (
        ('A collapsed fieldset', {
            'classes': ('collapse',),
            'fields': [('test_ip', 'test_url'), 'test_date',]
        }),
    )

class TestThatTabularInline(admin.TabularInline):
    model = TestThat

class TestSortableInline(admin.StackedInline, SortableInline):
    model = TestSortable
    extra = 0

class TestSortableAdmin(admin.ModelAdmin):
    model = TestSortable

class TestMeAdmin(admin.ModelAdmin):
    list_display = ['test_ip', 'test_url', 'test_int', 'test_img', 'test_file', 'test_date', 'test_char', 'test_bool', 'test_time', 'test_slug', 'test_text', 'test_email', 'test_float', 'test_bigint', 'test_positive_integer', 'test_decimal', 'test_comma_separated_int', 'test_small_int', 'test_nullbool', 'test_filepath', 'test_positive_small_int', ]
    search_fields = ['test_int', ]
    list_editable = ['test_int', ]
    list_filter = ['test_ip', 'test_url', 'test_int', ]
    list_per_page = 3
    date_hierarchy = 'test_date'
    actions = ['useless_action']
    inlines = [TestThatStackedInline, TestThatTabularInline, TestSortableInline]
    save_as = True
    save_on_top = True

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple }
    }

    def useless_action(self, request, queryset):
        self.message_user(request, "Useless action successfully executed.")


class TestMeAdminFieldsets(TestMeAdmin):
    actions_on_bottom = True
    inlines= [TestThatStackedFieldsetInline]
    fieldsets = (
        ('A fieldset', {
            'fields': ['test_m2m', 'test_ip', 'test_url', 'test_int', 'test_img', 'test_file', 'test_date', 'test_char', 'test_bool', 'test_time', 'test_slug', 'test_text', ],
        }),
        ('Another fieldset', {
            'fields': [('test_email', 'test_float'), 'test_bigint', ('test_positive_integer', 'test_decimal'), ('test_comma_separated_int', 'test_small_int'),],
        }),
        ('A collapsed fieldset', {
            'classes': ('collapse',),
            'fields': [('test_nullbool', 'test_filepath'), 'test_positive_small_int',]
        })
    )

admin.site.register(TestMeProxyForFieldsets, TestMeAdminFieldsets)
admin.site.register(TestMe, TestMeAdmin)
admin.site.register(TestSortable, TestSortableAdmin)
