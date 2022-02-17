from django.urls import path, include
from rest_framework import routers

from .views import FieldValuesSuggestionViewSet

router = routers.DefaultRouter()
router.register('field-values-suggestion', FieldValuesSuggestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]