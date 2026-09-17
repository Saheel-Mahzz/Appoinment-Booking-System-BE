from django.shortcuts import render
from rest_framework import viewsets

from services.models import ServiceModel
from services.serializers import ServiceModelSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceModelSerializer