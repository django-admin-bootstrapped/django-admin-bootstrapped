class SortableInline:
    sortable_field_name = "position"

    class Media:
        js = (
            '/static/admin/js/jquery.sortable.js',
        )

        css = {
            'all':('/static/admin/css/admin-inlines.css',)
        }

class CollapsibleInline:
    start_collapsed = False