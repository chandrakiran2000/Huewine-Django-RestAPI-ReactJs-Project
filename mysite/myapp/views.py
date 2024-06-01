from django.shortcuts import render
from rest_framework import viewsets
from .models import Moviesdata
from .serializers import MoviesdataSerializer

# Create your views here.

class MoviesdataViewSet(viewsets.ModelViewSet):
    queryset = Moviesdata.objects.all()
    serializer_class = MoviesdataSerializer