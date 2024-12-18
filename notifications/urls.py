from django.conf import settings
from django.urls import include, re_path, path
from rest_framework.routers import DefaultRouter

from notifications.views import NotificationViewSet

router = DefaultRouter()
router.register("notification", NotificationViewSet, basename="notification")


urlpatterns = [
    re_path('', include(router.urls)),
]
