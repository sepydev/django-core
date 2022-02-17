from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q

from ..models import AbstractModel, AbstractManager, TitleDescriptionModelMixin


class FieldValuesSuggestionManager(AbstractManager):
    pass


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
        limit_choices_to=content_type_limits()
    )
    field = models.CharField(
        max_length=500,
    )

    class Meta:
        verbose_name = "Field values suggestion"
        verbose_name_plural = "Field values suggestions"
