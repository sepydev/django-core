from django.contrib.admin import ModelAdmin


class AbstractAdmin(ModelAdmin):
    list_display = [
        'pk',
        'is_active',
    ]
    fields = [
        'is_active',
        'create_date',
    ]
    readonly_fields = [
        'create_date',
    ]
    raw_id_fields = []
