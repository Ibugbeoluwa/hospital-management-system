from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.


# Customize the display of our custom User model in Django Admin
class CustomUserAdmin(UserAdmin):
    model = User
    # Display the username, email, role, and staff status in the list table
    list_display = ['username', 'email', 'role', 'is_staff', 'is_superuser']
    
    # Add 'role' to the user edit page inside Admin
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Role', {'fields': ('role',)}),
    )

# Register our custom user model with the custom admin class
admin.site.register(User, CustomUserAdmin)