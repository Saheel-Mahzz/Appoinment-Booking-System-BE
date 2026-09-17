from django.urls import include
from rest_framework.routers import DefaultRouter, path
from services.views import ServiceViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet, basename='service')

urlpatterns = [
    path('', include(router.urls)),
]