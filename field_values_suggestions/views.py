from django_filters import rest_framework as filters

from helpers.swagger import ViewSetTagDecorator
from users.permisions import DjangoModelPermission
from .filters import SuggestionFilter
from .models import FieldValuesSuggestion as FieldValuesSuggestionModel
from .serializers import FieldValuesSuggestionSummarySerializer, FieldValuesSuggestionDetailSerializer
from ..views import ModelViewSet


@ViewSetTagDecorator(tags=("Field Values Suggestion",))
class FieldValuesSuggestionViewSet(ModelViewSet):
    queryset = FieldValuesSuggestionModel.objects.all()
    permission_classes = (DjangoModelPermission,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SuggestionFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return FieldValuesSuggestionDetailSerializer
        else:
            return FieldValuesSuggestionSummarySerializer
