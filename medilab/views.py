from django.shortcuts import render, redirect
from django.http import JsonResponse
from medilab.models import Doctor, FAQ, Testimonial, Gallery, Contact
from doctor.models import Doctorprofile, Department
from .forms import ContactForm, AppointmentForm, NewlettersForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from user.decorators import allowed_users
from django.template.loader import render_to_string
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# @allowed_users(allowed_roles=['admin'])
def index(request):
    departments = Department.objects.all()
    doctors = Doctorprofile.objects.all()
    FAQs = FAQ.objects.all()
    testimonials = Testimonial.objects.all()
    galleries = Gallery.objects.all()
    contactform = ContactForm(request=request)
    appointmentform = AppointmentForm(request=request)
    subscribeform = NewlettersForm()
    if request.method == 'POST':
        contactform = ContactForm(request.POST, request=request)
        appointmentform = AppointmentForm(request.POST, request=request)
        subscribeform = NewlettersForm(request.POST)
        if contactform.is_valid():
            cont_form = contactform.save(commit=False)
            cont_form.save()
            messages.success(request, 'Your message has been sent successfully. Thank you!')
            return redirect('medilab:index')
        if appointmentform.is_valid():
            app_form = appointmentform.save(commit=False)
            if request.user.is_authenticated:
                app_form.owner = request.user.profile

            # Render the new appointment as an HTML snippet
            context = {
                'appointment': app_form
            }
            new_appointment_html = render_to_string('doctor/appointment_row.html', context)

            # Trigger websocket event
            channel_layer = get_channel_layer()
            doctor_id = app_form.doctor.id  # Assuming app_form.doctor is the Doctorprofile object
            async_to_sync(channel_layer.group_send)(
                f'doctor_{doctor_id}',
                {
                    'type': 'send_new_appointment',
                    'appointment': new_appointment_html
                }
            )

            app_form.save()
            messages.success(request, 'Your appointment has been made successfully. Thank you!')
            return redirect('medilab:index')
        if subscribeform.is_valid():
            print('test4')
            sub_form = subscribeform.save(commit=False)
            sub_form.save()
            print(sub_form.email)

            subject = 'Thank you for Subscribe to Medilab'
            message = 'We are glad you are here!'

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [sub_form.email],
                fail_silently=False,
            )

            messages.success(request, 'Thank you for Subscribe!')
            return redirect('medilab:index')
        messages.error(request, 'Please check the form information again!')

    context = {'departments': departments, 'doctors': doctors, 'FAQs': FAQs,
               'testimonials': testimonials, 'galleries': galleries,
               'contactform': contactform, 'appointmentform': appointmentform, 'subscribeform': subscribeform}
    return render(request, 'index.html', context)

def get_department(request):
    doctor_id = request.GET.get('doctor_id')
    department = Doctorprofile.objects.get(id=doctor_id).department

    return JsonResponse({'department_id': department.id})
# Create your views here.
