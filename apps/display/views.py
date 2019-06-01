from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .serializers import PhotoSerializer
from .models import Photo


class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows photos to be viewed
    """
    queryset = Movie.objects.all().order_by('title')
    serializer_class = PhotoSerializer
