from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MediaViewSet

# Create router and register viewsets
router = DefaultRouter()
router.register(r'media', MediaViewSet, basename='media')

app_name = 'wedding_gallery'

urlpatterns = [
    path('/api/', include(router.urls)),
]
