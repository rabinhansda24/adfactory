from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from home.models import *

# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
        """
    queryset = BlogDetails.objects.all()
    serializer_class = BlogSerializer


class AdViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
        """
    queryset = AdDetails.objects.all()
    serializer_class = AdSerializer