from rest_framework import routers

from posts.api import viewsets

Post_router = routers.DefaultRouter()
Post_router.register('post', viewsets.PostViewSet)
