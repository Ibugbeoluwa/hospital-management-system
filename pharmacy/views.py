from django.shortcuts import render, redirect
from .models import Medicine, Prescription
from .forms import MedicineForm, PrescriptionForm

# Create your views here.
def index(request):
    medicines = Medicine.objects.all()
    prescriptions = Prescription.objects.all()
    return render(request, 'pharmacy/index.html', {
        'medicines': medicines,
        'prescriptions': prescriptions
    })

def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pharmacy:index')
    else:
        form = MedicineForm()
    return render(request, 'pharmacy/add_medicine.html', {'form': form})

def add_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save()
            
            # Bonus logic: Reduce drug stock count by 1 when prescribed!
            medicine = prescription.medicine
            if medicine.stock_quantity > 0:
                medicine.stock_quantity -= 1
                medicine.save()
                
            return redirect('pharmacy:index')
    else:
        form = PrescriptionForm()
    return render(request, 'pharmacy/add_prescription.html', {'form': form})