from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from pharmacy.models import Medicine, Prescription

@login_required(login_url='accounts:login')
def index(request):
    patient_count = Patient.objects.count()
    doctor_count = Doctor.objects.count()
    appointment_count = Appointment.objects.count()
    medicine_count = Medicine.objects.count()
    prescription_count = Prescription.objects.count()

    low_stock = Medicine.objects.filter(stock_quantity__lte=5)

    context = {
        'patient_count': patient_count,
        'doctor_count': doctor_count,
        'appointment_count': appointment_count,
        'medicine_count': medicine_count,
        'prescription_count': prescription_count,
        'low_stock': low_stock,
    }

    return render(request, 'dashboard/index.html', context)