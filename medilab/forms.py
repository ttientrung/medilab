from django import forms
from .models import Contact, Appointment, Doctor, Department, Newletters
from doctor.models import Doctorprofile
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    r"((\([0-9]{3}\)[0-9]{9,15})|([0-9]{10,15}))", "Your number must be (xxx)xxxxxxxxx or 0xxxxxxxxx!"
)

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'placeholder': 'Your Name',
        'type': 'text',
        'name': 'name',
        'id': 'name',
        'class': 'form-control',
        'required': 'True'}))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email',
        'type': 'email',
        'name': 'email',
        'id': 'email',
        'class': "form-control",
        'required': 'True',
    }))

    subject = forms.CharField(max_length=264, widget=forms.TextInput(attrs={
        'placeholder': 'Subject',
        'type': 'text',
        'name': 'subject',
        'id': 'subject',
        'class': 'form-control',
        'required': 'True'}))
    
    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
        'placeholder': 'Message',
        'name': 'message',
        'class': 'form-control',
        'row': '5',
        'required': 'True'}))
    
    class Meta:
        model = Contact
        # fields = '__all__'
        exclude = ['created_day']
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(ContactForm, self).__init__(*args, **kwargs)
        if self.request.user.is_authenticated:
            self.fields['name'].initial = self.request.user.first_name
            self.fields['email'].initial = self.request.user.email

class AppointmentForm(forms.ModelForm):
    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'placeholder': 'Your Name',
        'type': 'text',
        'name': 'name',
        'id': 'name',
        'class': 'form-control',
        'data-rule': 'minlen:4',
        'data-msg': 'Please enter at least 4 chars'}))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email',
        'type': 'email',
        'name': 'email',
        'id': 'email',
        'class': "form-control",
        'data-rule': 'email',
        'data-msg': 'Please enter a valid email'}))
    
    phone_number = forms.CharField(max_length=20, validators=[phone_validator], widget=forms.TextInput(attrs={
        'placeholder': 'Your Phone',
        'type': 'number',
        'name': 'phone',
        'id': 'phone',
        'class': "form-control",
        'data-rule': 'minlen:4',
        'data-msg': 'Please enter at least 4 chars',
        'pattern': "((\([0-9]{3}\)[0-9]{9,15})|([0-9]{10,15}))",
        'title': "Your phone number must be (xxx)xxxxxxxxx or 0xxxxxxxxx"
    }))

    appointment_date = forms.DateField(widget=forms.DateInput(attrs={
        'placeholder': 'Appointment Date',
        'type': 'date',
        'name': 'date',
        'id': 'date',
        'class': "form-control",
        'data-rule': 'minlen:4',
        'data-msg': 'Please enter at least 4 chars'
    }))

    department = forms.ModelChoiceField(queryset=Department.objects.all(), label='Department', required=False, widget=forms.Select(attrs={
        'placeholder': 'Select Department',
        'name': 'department',
        'id': 'department',
        'class': "form-select",
    }))

    doctor = forms.ModelChoiceField(queryset=Doctorprofile.objects.all(), label='Doctor', widget=forms.Select(attrs={
        'placeholder': 'Select Doctor',
        'name': 'doctor',
        'id': 'doctor',
        'class': "form-select",
    }))

    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
        'placeholder': 'Message (optional)',
        'name': 'message',
        'class': 'form-control',
        'row': '5'
    }))

    class Meta:
        model = Appointment
        exclude = ['created_day']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(AppointmentForm, self).__init__(*args, **kwargs)
        if self.request.user.is_authenticated:
            self.fields['name'].initial = self.request.user.first_name
            self.fields['email'].initial = self.request.user.email
        # self.fields['department'].initial = Doctorprofile.objects.all()[0].department
        # self.fields['doctor'].initial = Doctorprofile.objects.all()[0]
        # self.fields['doctor'].queryset = self.get_department().doctor_set.all()
    
    # def get_department(self):
    #     department_id = self['department'].value()
    #     department = Department.objects.get(id=department_id)
    #     return department

class NewlettersForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email',
        'type': 'email',
        'name': 'email',
        'id': 'email',
        'class': "form-control",
        'data-rule': 'email',
        'data-msg': 'Please enter a valid email'}))
    class Meta:
        model = Newletters
        exclude = ['email']
