from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('', include(('posts.urls', 'posts'), namespace='posts')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
