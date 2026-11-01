from django.urls import path
from . import views

app_name = "appointments"

urlpatterns = [
    path("", views.index, name="index"),       
    path("add", views.add_appointment, name="add_appointment"),
    path('<int:pk>/', views.detail, name='detail'),                # /appointments/1/
    path('<int:pk>/edit/', views.update_status, name='update_status'), 
]