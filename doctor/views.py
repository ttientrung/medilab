from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, Group
from .forms import doctorProfileForm
from user.models import Profile
from medilab.models import Appointment


@login_required(login_url='user:login-register')
def doctorAccount(request):
    page = 'doctor-account'
    profile = request.user.doctorprofile
    profileForm = doctorProfileForm(instance=profile)
    if request.method == 'POST':
        profileForm = doctorProfileForm(request.POST, request.FILES, instance=profile)
        if profileForm.is_valid():
            profile = profileForm.save()
            messages.success(request, 'Your profile was update successfully!')
            return redirect('doctor:doctor-account')
        else:
            messages.error(request, 'Please check your information form!')
    context = {'profile': profile, 'profileForm': profileForm, 'page': page}
    return render(request, 'doctor/doctor_account_form.html', context)

@login_required(login_url='user:login-register')
def doctorAccountAppointment(request):
    page = 'doctor-account'
    profile = request.user.doctorprofile
    appointments = Appointment.objects.filter(doctor=profile)
    context = {'profile': profile, 'appointments': appointments, 'page': page}
    return render(request, 'doctor/doctor_account_appointment.html', context)
