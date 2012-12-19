class SortableInline:
    sortable_field_name = "position"
    collapse_stacked = True

    class Media:
        js = (
            '/static/admin/js/jquery.sortable.js',
        )

        css = {
            'all':('/static/admin/css/admin-inlines.css',)
        }