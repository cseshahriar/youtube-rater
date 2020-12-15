from django.urls import path, include
from rest_framework import routers

# routers
router = routers.DefaultRouter()
# router.registry('videos', VideoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
