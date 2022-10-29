from rest_framework import pagination, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ads.models.ad import Ad
from ads.models.comment import Comment
from ads.permissions import IsOwner, IsAdmin
from ads.serializers.comment import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        ad_id = self.kwargs.get("ad_pk")
        ad = get_object_or_404(Ad, id=ad_id)
        serializer.save(author=self.request.user, ad=ad)

    def get_queryset(self):
        ad = get_object_or_404(Ad, id=self.kwargs.get('ad_pk'))
        return ad.comments.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = (IsAuthenticated,)
        elif self.action in ['create', 'update', 'partial_update', "destroy"]:
            permission_classes = (IsOwner | IsAdmin, )
        return tuple(perm() for perm in permission_classes)