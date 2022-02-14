from rest_framework import serializers


class AbstractSummarySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['pk', 'is_active']
        read_only_fields = []
        abstract = True


class AbstractDetailSerializer(AbstractSummarySerializer):
    class Meta:
        fields = [
                     'create_date'
                 ] + AbstractSummarySerializer.Meta.fields
        read_only_fields = [
                               'create_date'
                           ] + AbstractSummarySerializer.Meta.read_only_fields
        abstract = True
