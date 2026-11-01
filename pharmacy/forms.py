from django import forms
from .models import Medicine, Prescription

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'category', 'stock_quantity', 'expiry_date']

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient', 'doctor', 'medicine', 'dosage', 'duration']