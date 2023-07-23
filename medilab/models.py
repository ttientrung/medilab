from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from user.models import Profile

class Department(models.Model):
    name = models.CharField(max_length= 200, null=True, blank=True)
    short_intro = models.CharField(max_length= 2000, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='departments/', default="department/default.jpg")

    def __str__(self):
        return str(self.name)
    
class Doctor(models.Model):
    name = models.CharField(max_length= 200, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    short_intro = models.CharField(max_length= 2000, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='doctors/', default="doctors/user-default.png")
    social_twitter = models.CharField(max_length=2000, null=True, blank=True)
    social_facebook = models.CharField(max_length=2000, null=True, blank=True)
    social_instagram = models.CharField(max_length=2000, null=True, blank=True)
    social_linkedin = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return str(self.name)
    
class FAQ(models.Model):
    question = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.question)
    
class Testimonial(models.Model):
    owner = models.CharField(max_length= 200, null=True, blank=True)
    owner_job = models.CharField(max_length= 200, null=True, blank=True)
    owner_image = models.ImageField(null=True, blank=True, upload_to='testimonials/', default="testimonials/user-default.png")
    testi = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.owner)
    
class Gallery(models.Model):
    name = models.CharField(max_length= 200, null=True, blank=True)
    gallery_image = models.ImageField(null=True, blank=True, upload_to='galleries/', default="galleries/default.jpg")

    def __str__(self):
        return str(self.name)
    
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=264)
    message = models.TextField()
    created_day = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject
    
class Appointment(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=17,null=True, blank=True)
    appointment_date = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    created_day = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name) + ' ' + str(self.appointment_date)
    
class Newletters(models.Model):
    email = models.EmailField()

# Create your models here.
