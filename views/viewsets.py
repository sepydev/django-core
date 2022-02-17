from rest_framework.viewsets import ModelViewSet as RestFrameworkModelViewSet


class ModelViewSet(RestFrameworkModelViewSet):
    pass


class OwnerListModelViewSetMixin:
    """Users are able to view their own objects"""

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class SetOwnerModelViewListMixin:
    """Set the owner of the object automatically based on the sender user (post request)"""

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
