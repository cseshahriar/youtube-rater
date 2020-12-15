from django.urls import path, include
from rest_framework import routers
from .views import VideoViewSet, RatingViewSet

# routers
router = routers.DefaultRouter()
router.register('videos', VideoViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls))
]
