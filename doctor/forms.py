from django import forms
from .models import Doctorprofile
from medilab.models import Department
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    r"((\([0-9]{3}\)[0-9]{9,15})|([0-9]{10,15}))", "Your number must be (xxx)xxxxxxxxx or 0xxxxxxxxx!"
)

class doctorProfileForm(forms.ModelForm):
    class Meta:
        model = Doctorprofile
        fields = ['name', 'email', 'phone_number', 'department', 'short_intro', 'bio', 'location', 'gender', 'age', 'profile_image', 'social_twitter', 'social_facebook', 'social_instagram', 'social_linkedin']
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'phone_number': 'Your Phone Number', 
            'department': 'Your Department',
            'short_intro': 'Short Intro',
            'bio': 'About You',
            'location': 'Your Location',
            'gender': 'Your Gender', 
            'age': 'Your Age',
            'social_twitter': 'Your Twitter',
            'social_facebook': 'Your Facebook',
            'social_instagram': 'Your Instagram',
            'social_linked': 'Your LinkedIn',
            'profile_image': 'Your Profile Image',
        }
    def __init__(self, *args, **kwargs):
        super(doctorProfileForm, self).__init__(*args, **kwargs)
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
        self.fields['department'].widget.attrs.update({
            'id': 'department',
            'placeholder': 'Your Department',
            'class': 'form-control',
        })
        self.fields['department'].queryset = Department.objects.all()
        self.fields['short_intro'].widget.attrs.update({
            'type': 'text',
            'id': 'short_intro',
            'placeholder': 'Short Intro',
            'class': 'form-control',
        })
        self.fields['bio'].widget.attrs.update({
            'type': 'text',
            'id': 'bio',
            'placeholder': 'About you',
            'class': 'form-control',
        })
        self.fields['bio'].max_length = 500
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
        self.fields['social_twitter'].widget.attrs.update({
            'type': 'text',
            'id': 'social_twitter',
            'placeholder': 'Your Twitter',
            'class': 'form-control',
        })
        self.fields['social_facebook'].widget.attrs.update({
            'type': 'text',
            'id': 'social_facebook',
            'placeholder': 'Your Facebook',
            'class': 'form-control',
        })
        self.fields['social_instagram'].widget.attrs.update({
            'type': 'text',
            'id': 'social_instagram',
            'placeholder': 'Your Instagram',
            'class': 'form-control',
        })
        self.fields['social_linkedin'].widget.attrs.update({
            'type': 'text',
            'id': 'social_linkedin',
            'placeholder': 'Your LinkedIn',
            'class': 'form-control',
        })