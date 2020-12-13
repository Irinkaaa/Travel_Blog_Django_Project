from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('Travel_blog.accounts.urls')),
    path('admin/', admin.site.urls),
    path('', include('Travel_blog.app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

