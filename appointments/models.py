from django.db import models
from patients.models import Patient
from doctors.models import Doctor

# Create your models here.

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    # Foreign Keys link this appointment to a real Patient and Doctor in the database
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    appointment_date = models.CharField(max_length=100, help_text="e.g. 01-11-2026")
    appointment_time = models.CharField(max_length=100, default='09:00 AM', help_text="e.g. 10:00 AM")
    reason = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.patient.first_name} with Dr. {self.doctor.name} on {self.appointment_date}"