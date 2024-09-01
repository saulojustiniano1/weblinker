from rest_framework import permissions, viewsets

from posts import models
from posts.api import serializers

from .permissions import IsInSpecificGroup


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsInSpecificGroup]
