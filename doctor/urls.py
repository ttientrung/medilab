from django.urls import path
from . import views

app_name = 'doctor'
urlpatterns = [
    path('doctor-account/', views.doctorAccount, name = "doctor-account"),
    path('doctor-account-appointment/', views.doctorAccountAppointment, name = "doctor-account-appointment"),
]