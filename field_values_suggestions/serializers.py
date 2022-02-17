from django.contrib.contenttypes.models import ContentType

from .models import FieldValuesSuggestion as FieldValuesSuggestionModel
from ..seralizers import AbstractSummarySerializer, AbstractDetailSerializer
from rest_framework import serializers


class ContentTypeField(serializers.Field):
    def to_representation(self, value):
        return value.app_label + "." + value.model

    def to_internal_value(self, data):
        app_label, model = data.split(".")
        return ContentType.objects.get(app_label=app_label, model=model)


class FieldValuesSuggestionSummarySerializer(AbstractSummarySerializer):
    content_type = ContentTypeField()

    class Meta:
        model = FieldValuesSuggestionModel
        fields = [
                     'content_type',
                     'field'
                 ] + AbstractSummarySerializer.Meta.fields
        read_only_fields = [
                           ] + AbstractSummarySerializer.Meta.read_only_fields


class FieldValuesSuggestionDetailSerializer(FieldValuesSuggestionSummarySerializer, AbstractDetailSerializer):
    class Meta:
        model = FieldValuesSuggestionModel
        fields = [] + \
                 FieldValuesSuggestionSummarySerializer.Meta.fields + \
                 AbstractSummarySerializer.Meta.fields

        read_only_fields = [] + \
                           FieldValuesSuggestionSummarySerializer.Meta.read_only_fields + \
                           AbstractSummarySerializer.Meta.read_only_fields
