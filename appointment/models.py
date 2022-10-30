from django.db import models
from account.models import User

# Create your models here.

class Apointment(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor")
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient")
    speciality = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def __str__(self):
        return f"{self.doctor} - {self.patient}"

    