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
