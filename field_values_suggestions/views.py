from ..views import ModelViewSet
from .models import FieldValuesSuggestion as FieldValuesSuggestionModel
from .serializers import FieldValuesSuggestionSummarySerializer, FieldValuesSuggestionDetailSerializer
from users.permisions import DjangoModelPermission


class FieldValuesSuggestionViewSet(ModelViewSet):
    queryset = FieldValuesSuggestionModel.objects.all()
    permission_classes = (DjangoModelPermission,)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return FieldValuesSuggestionDetailSerializer
        else:
            return FieldValuesSuggestionSummarySerializer
