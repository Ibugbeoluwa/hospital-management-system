from django.db import models

# Create your models here.
from django.db import models


class Doctor(models.Model):
    # Choices for Department (10 choices)
    DEPARTMENT_CHOICES = [
        ("General Medicine", "General Medicine"),
        ("Pediatrics", "Pediatrics"),
        ("Cardiology", "Cardiology"),
        ("Surgery", "Surgery"),
        ("Orthopedics", "Orthopedics"),
        ("Obstetrics & Gynecology", "Obstetrics & Gynecology"),
        ("Neurology", "Neurology"),
        ("Dermatology", "Dermatology"),
        ("Psychiatry", "Psychiatry"),
        ("Radiology", "Radiology"),
    ]

    # Choices for Specialization (10 choices mapped across major fields)
    SPECIALIZATION_CHOICES = [
        ("Internal Medicine", "Internal Medicine"),
        ("Pediatric Cardiology", "Pediatric Cardiology"),
        ("Interventional Cardiology", "Interventional Cardiology"),
        ("General Surgery", "General Surgery"),
        ("Orthopedic Surgery", "Orthopedic Surgery"),
        ("Maternal-Fetal Medicine", "Maternal-Fetal Medicine"),
        ("Clinical Neurophysiology", "Clinical Neurophysiology"),
        ("Cosmetic Dermatology", "Cosmetic Dermatology"),
        ("Child & Adolescent Psychiatry", "Child & Adolescent Psychiatry"),
        ("Interventional Radiology", "Interventional Radiology"),
    ]

    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    specialization = models.CharField(
        max_length=100, choices=SPECIALIZATION_CHOICES
    )
    phone = models.CharField(max_length=15)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization} ({self.department})"