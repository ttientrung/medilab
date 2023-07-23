from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    r"((\([0-9]{3}\)[0-9]{9,15})|([0-9]{10,15}))", "Your number must be (xxx)xxxxxxxxx or 0xxxxxxxxx!"
)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'type': 'text',
            'placeholder': 'Your name',
            'required': 'True'
        })
        self.fields['username'].widget.attrs.update({
            'type': 'text',
            'placeholder': 'User name',
            'required': 'True'
        })
        self.fields['email'].widget.attrs.update({
            'type': 'text',
            'placeholder': 'Email address',
            'required': 'True'
        })
        self.fields['password1'].widget.attrs.update({
            'type': 'password',
            'placeholder': 'Password',
            'required': 'True'
        })
        self.fields['password2'].widget.attrs.update({
            'type': 'password',
            'placeholder': 'Password confirmation',
            'required': 'True'
        })


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'phone_number', 'location', 'gender', 'age', 'profile_image']
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'phone_number': 'Your Phone Number', 
            'location': 'Your Location',
            'gender': 'Your Gender', 
            'age': 'Your Age',
            'profile_image': 'Your Profile Image',
        }
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'type': 'text',
            'id': 'name',
            'placeholder': 'Your name',
            'class': 'form-control',
            'required': 'True'
        })
        self.fields['email'].widget.attrs.update({
            'type': 'email',
            'id': 'email',
            'placeholder': 'Your email',
            'class': 'form-control',
            'aria-describedby': 'emailHelp',
            'required': 'True'
        })
        self.fields['phone_number'].validators.append(phone_validator)
        self.fields['phone_number'].widget.attrs.update({
            'type': 'number',
            'id': 'phone_number',
            'placeholder': 'Your phone',
            'class': 'form-control',
            'aria-describedby': 'phonelHelp',
            'required': 'True'
        })
        self.fields['age'].widget.attrs.update({
            'type': 'number',
            'id': 'age',
            'placeholder': 'Your age',
            'class': 'form-control',
            'required': 'True'
        })
        self.fields['gender'].widget.attrs.update({
            'id': 'gender',
            'placeholder': 'Your gender',
            'class': 'form-control',
            'required': 'True'
        })
        self.fields['gender'].choices = [
            ('male','Male'),
            ('female','Female'),
        ]
        self.fields['location'].widget.attrs.update({
            'type': 'text',
            'id': 'location',
            'placeholder': 'Your location',
            'class': 'form-control',
            'required': 'True'
        })
        self.fields['profile_image'].widget.attrs.update({
            'type': 'file',
            'id': 'profile_image',
            'placeholder': 'Your profile image',
            'class': 'form-control',
        })



        

