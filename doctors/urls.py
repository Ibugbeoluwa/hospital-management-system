from django.urls import path
from . import views

app_name = "doctors"

urlpatterns = [
    path("", views.index, name="index"),        
    path("add/", views.add_doctor, name="add_doctor"), 
    path('<int:pk>/', views.detail, name='detail'),
]