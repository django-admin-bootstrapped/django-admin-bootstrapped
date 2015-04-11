from django.contrib import admin
from collections import OrderedDict
import json

class SortableInline(object):
    sortable_field_name = "position"

    class Media:
        js = (
            'admin/js/jquery.sortable.js',
        )

        css = {
            'all': ('admin/css/admin-inlines.css', )
        }

class CollapsibleInline(object):
    start_collapsed = False


class TabPanelMixin(object):
    """Adds tabs to add/change form views in ModelAdmin"""

    tabs = ()
    """List of defined tabs.
    Each tab is defined by a tuple: ('tab_name', list_of_elements_to_contain)
    Example:
    tabs = [('Tab_name', ['fieldset_name', InlineClass]), #Other tabs...]
    """

    tabs_pos = 'top'
    """Tabs position ('top', 'left', 'right' or 'bottom')"""

    def _tabs_context(self, extra_context):
        if self.fieldsets is not None:
            fsets_order = [x[0] for x in self.fieldsets]
        else:
            fsets_order = []

        tabs = OrderedDict()
        for k in self.tabs:
            tab_name, tab_content = k
            tabs[tab_name] = []
            for v in tab_content:
                sel = ''

                if (v is None or fsets_order.count(v)):
                    sel = fsets_order.index(v), 'f'
                else:
                    # Inline
                    sel = self.inlines.index(v), 'i'

                tabs[tab_name].append(sel)

        extra_context = extra_context or {}
        extra_context['tabs'] = json.dumps(tabs)
        extra_context['tabs_pos'] = self.tabs_pos

        return extra_context

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = self._tabs_context(extra_context)
        return super(TabPanelMixin, self).change_view(request, object_id,
                                                      form_url,
                                                      extra_context=extra_context)

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = self._tabs_context(extra_context)
        return super(TabPanelMixin, self).add_view(request, form_url,
                                                   extra_context=extra_context)
