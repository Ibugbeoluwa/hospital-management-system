from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor
from .forms import DoctorForm

# Create your views here.



# 1. Show all doctors from database
def index(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/index.html', {'doctors': doctors})

# 2. Add a new doctor
def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save() # Saves straight to SQLite database
            return redirect('doctors:index')
    else:
        form = DoctorForm()

    return render(request, 'doctors/add.html', {'form': form})

# 3. View individual doctor profile
def detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctors/detail.html', {'doctor': doctor})