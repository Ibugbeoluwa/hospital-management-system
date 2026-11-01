from django.urls import path
from . import views

app_name = "patients"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_patient, name = "add_patient"),
    path('<int:pk>/', views.patient_detail, name='patient_detail'),    
    path('<int:pk>/edit/', views.patient_update, name='patient_update'),
]

