from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Role choices listed in your brief
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('DOCTOR', 'Doctor'),
        ('NURSE', 'Nurse'),
        ('RECEPTIONIST', 'Receptionist'),
        ('PHARMACIST', 'Pharmacist'),
        ('LAB_TECH', 'Lab Technician'),
        ('PATIENT', 'Patient'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='PATIENT')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"