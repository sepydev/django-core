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


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)
