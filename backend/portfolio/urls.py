"""
URL configuration for portfolio project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def api_root(request):
    """Root endpoint that provides API information"""
    return JsonResponse({
        'message': 'Portfolio API Server',
        'version': '1.0',
        'endpoints': {
            'admin': '/admin/',
            'api_root': '/api/',
            'about': '/api/about/',
            'experiences': '/api/experiences/',
            'projects': '/api/projects/',
            'skills': '/api/skills/',
            'education': '/api/education/',
            'contact': '/api/contact/',
            'social_links': '/api/social-links/',
            'awards': '/api/awards/',
            'hobbies': '/api/hobbies/',
        },
        'frontend': 'http://localhost:3001',
        'documentation': 'Access /api/ for API browser interface'
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

