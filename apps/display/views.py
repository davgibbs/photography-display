from django.shortcuts import render

from rest_framework import viewsets

from .serializers import PhotoSerializer
from .models import Photo


class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows photos to be viewed
    """
    queryset = Photo.objects.all().order_by('id')
    serializer_class = PhotoSerializer


def index(request):
    """
    Base index on what to show when user comes to base
    :param request: request object
    :return: redirect to the correct page
    """
    return render(request, 'display/index.html', {})
