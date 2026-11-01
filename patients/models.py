from django.db import models
import uuid

class Patient(models.Model):
    # Choices for dropdown menus
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    ]

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]

    # Database columns (fields)
    hospital_number = models.CharField(max_length=20, unique=True, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES, blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    next_of_kin = models.CharField(max_length=100)
    next_of_kin_phone = models.CharField(max_length=15)
    
    is_active = models.BooleanField(default=True)

    # Automatically generate a unique hospital ID (like HOSP-4A2B) when saving
    def save(self, *args, **kwargs):
        if not self.hospital_number:
            self.hospital_number = f"IB-{uuid.uuid4().hex[:4].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.hospital_number})"