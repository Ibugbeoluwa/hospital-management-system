from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Patient
from .forms import PatientForm
# Create your views here.

# 1. Show all patients (with simple text search)
@login_required
def index(request):
    # Only Admin, Doctor, Nurse, and Receptionist should see patient lists
    allowed_roles = ['ADMIN', 'DOCTOR', 'NURSE', 'RECEPTIONIST']
    if request.user.role not in allowed_roles:
        return HttpResponseForbidden("You do not have permission to view this page.") # Returns 403 status (Slide 6 & brief)
    
    # Read search term typed by the user in the HTML search box
    search_query = request.GET.get('q', '')

    if search_query:
        # Filter patients whose first name contains the search term
        patients = Patient.objects.filter(first_name__icontains=search_query)
    else:
        # Fetch every patient from the database
        patients = Patient.objects.all()

    return render(request, 'patients/index.html', {
        'patients': patients,
        'search_query': search_query
    })

# 2. Register a new patient
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            # Save the patient into SQLite database
            patient = form.save()
            # Redirect to their new detail page
            return redirect('patients:patient_detail', pk=patient.pk)
    else:
        form = PatientForm()

    return render(request, 'patients/add.html', {'form': form, 'title': 'Register New Patient'})

# 3. View single patient details (/patients/1/, /patients/2/, etc.)
def patient_detail(request, pk):
    # get_object_or_404 fetches the patient by Primary Key (pk), or gives 404 page if not found
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patients/patient_detail.html', {'patient': patient})

# 4. Edit an existing patient
def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    
    if request.method == 'POST':
        # instance=patient tells Django to update this specific existing patient
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patients:patient_detail', pk=patient.pk)
    else:
        # Pre-fill form with current patient data
        form = PatientForm(instance=patient)

    return render(request, 'patients/add.html', {'form': form, 'title': 'Edit Patient Details'})