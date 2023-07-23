from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, Group
from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile
from medilab.models import Appointment
from medilab.forms import AppointmentForm

def loginUser(request):
    page = 'login'
    formSignup = CustomUserCreationForm()
    if request.user.is_authenticated:
        return redirect('medilab:index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            if request.user.groups.all()[0].name == 'doctor':
                messages.info(request, 'Welcome back')
                # return HttpResponse('You are not authorized to view this page')
                return redirect('doctor:doctor-account')
            else:
                messages.info(request, 'Welcome back')
                return redirect('user:user-account')
            
        else:
            messages.error(request, 'Username Or Password is incorrect')
    context = {'page': page, 'formSignup': formSignup}
    return render(request, 'user/login_register.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('medilab:index')

def registerUser(request):
    page = 'register'
    formSignup = CustomUserCreationForm()
    if request.method == 'POST':
        formSignup = CustomUserCreationForm(request.POST)
        if formSignup.is_valid():
            user = formSignup.save(commit=False)
            user.username = user.username.lower()
            user.save()

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            
            messages.success(request, 'User account was created')
            login(request, user)
            return redirect('medilab:index')
        else:
            messages.error(request, 'An error has occurred during registration')
    context = {'page': page, 'formSignup': formSignup}
    return render(request, 'user/login_register.html', context)

@login_required(login_url='user:login-register')
def userAccount(request):
    page = 'account'
    profile = request.user.profile
    profileForm = ProfileForm(instance=profile)
    if request.method == 'POST':
        profileForm = ProfileForm(request.POST, request.FILES, instance=profile)
        if profileForm.is_valid():
            profileForm.save()
            messages.success(request, 'Your profile was update successfully!')
            return redirect('user:user-account')
        else:
            messages.error(request, 'Please check your information form!')
    context = {'profile': profile, 'profileForm': profileForm, 'page': page}
    return render(request, 'user/user_account_form.html', context)

@login_required(login_url='user:login-register')
def userAccountAppointment(request):
    page = 'account'
    profile = request.user.profile
    # appointmentform = AppointmentForm()
    appointments = Appointment.objects.filter(owner=profile)
    print(appointments)
    context = {'profile': profile, 'appointments': appointments, 'page': page}
    return render(request, 'user/user_account_appointment.html', context)

@login_required(login_url='user:login-register')
def appointmentUpdate(request, pk):
    profile = request.user.profile
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request=request, instance=appointment)
        print(form.errors)
        if form.is_valid():
            app_form = form.save(commit=False)
            app_form.owner = profile
            app_form.save()
            messages.success(request, 'Your appointment was update successfully!')
            return redirect('user:user-account-appointment')
    else:
        form = AppointmentForm(request=request, instance=appointment)
    context = {'appointment': appointment, 'form': form}
    return render(request, 'appointment_update.html', context)

@login_required(login_url='user:login-register')
def appointmentDelete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Your appointment was deleted successfully!')
        return redirect('user:user-account')
    context = {}
    return render(request, 'appointment_delete.html', context)
# Create your views here.
