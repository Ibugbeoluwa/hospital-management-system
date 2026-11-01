from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

# Form to register new users with a selected role
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role']

# Standard Django login form
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))