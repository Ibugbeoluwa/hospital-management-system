from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient  
        fields = [       
            'first_name', 'last_name', 'age', 'gender', 
            'phone', 'address', 'blood_group', 'allergies', 
            'next_of_kin', 'next_of_kin_phone'
        ]