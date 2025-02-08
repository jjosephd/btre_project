from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# URL patterns for the project
urlpatterns = [
    # Include URLs from the 'pages' app
    path('', include('pages.urls')),
    # Include URLs from the 'listings' app
    path('listings/', include('listings.urls')),
    # Admin site URLs
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
