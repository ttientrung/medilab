from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('login-register/', views.loginUser, name = "login-register"),
    path('register/', views.registerUser, name = "register"),
    path('logout/', views.logoutUser, name = "logout"),
    path('user-account/', views.userAccount, name = "user-account"),
    path('user-account-appointment/', views.userAccountAppointment, name = "user-account-appointment"),
    path('appointment-update/<str:pk>/', views.appointmentUpdate, name = "appointment-update"),
    path('appointment-delete/<str:pk>/', views.appointmentDelete, name = "appointment-delete"),
]