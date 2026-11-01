from django.urls import path
from . import views

app_name = "pharmacy"

urlpatterns = [
    path("", views.index, name="index"),                           
    path("add-medicine", views.add_medicine, name="add_medicine"), 
    path("add-prescription", views.add_prescription, name="add_prescription"), 
]