from django.contrib.contenttypes.models import ContentType
from django_filters import rest_framework as filters

from .models import FieldValuesSuggestion as FieldValuesSuggestionModel


class SuggestionFilter(filters.FilterSet):
    content_type = filters.CharFilter(field_name="content_type", method='get_content_type')

    def get_content_type(self, queryset, field_name, value):
        app_label, model = value.split(".")
        print(app_label, model)
        _content_type = ContentType.objects.get(app_label=app_label, model=model)
        return queryset.filter(content_type=_content_type)

    class Meta:
        model = FieldValuesSuggestionModel
        fields = ['content_type', 'field']
