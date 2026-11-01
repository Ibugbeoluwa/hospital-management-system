from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, CustomLoginForm

# Create your views here.
# 1. Login View
def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user) # Starts user session
            return redirect('dashboard:index') # Send logged-in user to dashboard
    else:
        form = CustomLoginForm()

    return render(request, 'accounts/login.html', {'form': form})

# 2. Logout View
def logout_view(request):
    logout(request) # Clears user session
    return redirect('accounts:login')

# 3. Register View
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Automatically log in new user after registration
            return redirect('dashboard:index')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})