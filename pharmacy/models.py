from django.db import models
from patients.models import Patient
from doctors.models import Doctor

# Create your models here.


# 1. Medicine Inventory Model
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    stock_quantity = models.PositiveIntegerField(default=0)
    expiry_date = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.stock_quantity} left)"

# 2. Prescription Model
class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    
    dosage = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    prescribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient.first_name} - {self.medicine.name}"