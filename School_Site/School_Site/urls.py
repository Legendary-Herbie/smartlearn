
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
# Serve static files during development
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('learn.urls')),
    path('', include('time_management.urls')),
    path('', include('recall.urls')),
]

# In production serve the React build's index.html for frontend routes
if not settings.DEBUG:
    # assumes the React build is located at BASE_DIR / 'school-templates-frontend' / 'build'
    urlpatterns += [re_path(r'^.*$', TemplateView.as_view(template_name='index.html'))]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
