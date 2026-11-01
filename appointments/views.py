from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
from .forms import AppointmentForm

# Create your views here.
# 1. List all appointments in database
def index(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/index.html', {'appointments': appointments})

# 2. Book a new appointment
def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save() # Saves appointment into SQLite database
            return redirect('appointments:index')
    else:
        form = AppointmentForm()

    return render(request, 'appointments/add.html', {'form': form})

# 3. View individual appointment details
def detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'appointments/detail.html', {'appointment': appointment})

# 4. Change status (e.g., Confirm, Complete, Cancel)
def update_status(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointments:detail', pk=appointment.pk)
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'appointments/add.html', {'form': form})