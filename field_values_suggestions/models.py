from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from ..models import AbstractModel, AbstractManager, TitleDescriptionModelMixin


class FieldValuesSuggestionManager(AbstractManager):
    def get_queryset(self):
        return super(FieldValuesSuggestionManager, self).get_queryset()


def content_type_limits():
    register_suggestion_models = getattr(settings, 'REGISTER_SUGGESTION_MODELS', None)
    limit = Q(pk=None)
    if register_suggestion_models:
        for (app_label, model) in register_suggestion_models:
            limit = limit | Q(app_label=app_label, model=model)
    return limit


class FieldValuesSuggestion(TitleDescriptionModelMixin, AbstractModel):
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        verbose_name="Content type",
        limit_choices_to=content_type_limits(),
    )
    field = models.CharField(
        max_length=500,
    )
    objects = FieldValuesSuggestionManager()

    class Meta:
        verbose_name = "Field values suggestion"
        verbose_name_plural = "Field values suggestions"

    def clean_fields(self, exclude=None):
        # Make sure only valid content types can be selected
        valid_content_types = ContentType.objects.filter(content_type_limits())
        if self.content_type not in valid_content_types:
            raise ValidationError(
                {
                    'content_type': ValidationError(_('Invalid content type'), code='invalid')
                }
            )

        # Make sure only valid field can be selected
        valid_fields = [field.name for field in self.content_type.model_class()._meta.fields]
        if self.field not in valid_fields:
            raise ValidationError(
                {
                    'field': ValidationError(_('Invalid field'), code='invalid')
                }
            )
