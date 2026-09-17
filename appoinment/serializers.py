from rest_framework import serializers

from appoinment.models import AppointmentModel


class AppointmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentModel
        fields = '__all__'
