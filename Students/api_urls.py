from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api_views

router = DefaultRouter()
router.register(r'students', api_views.StudentViewSet)
router.register(r'progress', api_views.ProgressViewSet)
router.register(r'appusage', api_views.AppUsageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]