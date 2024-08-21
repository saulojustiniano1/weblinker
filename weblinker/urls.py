from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from posts.api.router import Post_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(Post_router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
