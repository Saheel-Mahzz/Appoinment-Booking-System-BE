from django.db import models

from services.models import ServiceModel


class AppointmentModel(models.Model):
    customer_name = models.CharField(max_length=100)
    service = models.ForeignKey(
        ServiceModel,
        on_delete=models.PROTECT,
        related_name='appointments',
    )
    customer_phone = models.CharField(max_length=20)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.customer_name} - {self.appointment_date} {self.appointment_time}'
