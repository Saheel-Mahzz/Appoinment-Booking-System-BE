from rest_framework import viewsets

from appoinment.models import AppointmentModel
from appoinment.serializers import AppointmentModelSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = AppointmentModel.objects.all()
    serializer_class = AppointmentModelSerializer
