from rest_framework import serializers

from services.models import ServiceModel


class ServiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = '__all__'