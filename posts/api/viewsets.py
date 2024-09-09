import logging

from rest_framework import permissions, viewsets

from posts import models
from posts.api import serializers

from .permissions import IsInSpecificGroup

logger = logging.getLogger('custom')


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    # permission_classes = [permissions.IsAuthenticated, IsInSpecificGroup]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        logger.info(f'Novo {self.request.data["title"]}')
        serializer.save()
