from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length= 200, null=True, blank=True)
    short_intro = models.CharField(max_length= 2000, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='departments/', default="department/default.jpg")

    def __str__(self):
        return str(self.name)

class Doctorprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length= 200, null=True, blank=True)
    email = models.EmailField(max_length= 500, null=True, blank=True)
    phone_number = models.CharField(max_length=17,null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    short_intro = models.CharField(max_length= 2000, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    username = models.CharField(max_length= 200, null=True, blank=True)
    location = models.CharField(max_length= 200, null=True, blank=True)
    gender = models.CharField( max_length=50,blank=True,choices=(('male','Male'), ('female','Female')))
    age = models.IntegerField(blank=True , null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='doctors/', default="doctors/user-default.png")
    social_twitter = models.CharField(max_length=2000, null=True, blank=True)
    social_facebook = models.CharField(max_length=2000, null=True, blank=True)
    social_instagram = models.CharField(max_length=2000, null=True, blank=True)
    social_linkedin = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)
    
    
