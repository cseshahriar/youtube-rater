from rest_framework import status, viewsets
from rest_framework.response import Response

from rest_framework.permissions import AllowAny

from .models import Video, Rating
from .serializers import VideoSerializer, RatingSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (AllowAny,)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (AllowAny,)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'Rating cannot be updated like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
