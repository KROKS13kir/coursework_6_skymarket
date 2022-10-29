from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.models.ad import Ad
from ads.permissions import IsOwner, IsAdmin
from ads.serializers.ad import AdSerializer, AdDetailSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

    def get_serializer_class(self):
        if self.action in ['retrieve', "create", "update", "partial_update", "destroy"]:
            return AdDetailSerializer
        else:
            return AdSerializer

    def get_permissions(self):
        permission_classes = (AllowAny,)
        if self.action == "retrieve":
            permission_classes == (AllowAny,)
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = (IsOwner | IsAdmin, )
        return tuple(perm() for perm in permission_classes)

    def get_queryset(self):
        if self.action == 'me':
            return Ad.objects.filter(author=self.request.user).all()
        return Ad.objects.all()

    @action(detail=False, methods=["get", ])
    def me(self, request, *args, **kwargs):
        return super().list(self, request, args, **kwargs)