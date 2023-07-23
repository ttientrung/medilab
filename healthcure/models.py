from django.db import models
from django.core.validators import RegexValidator

class BreastCancer(models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=17,null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    gender = models.CharField( max_length=50,blank=True,choices=(('female','Female'),('male','Male')))
    age = models.IntegerField(blank=True , null=True)
    concave_points_mean = models.FloatField()
    area_mean = models.FloatField()
    radius_mean = models.FloatField()
    perimeter_mean = models.FloatField()
    concavity_mean = models.FloatField()

class Diabetes(models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=17,null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    gender = models.CharField( max_length=50,blank=True,choices=(('female', 'Female'),('male', 'Male')))
    number_of_pregnancies = models.FloatField()
    glucose_conc = models.FloatField()
    blood_pressure = models.FloatField()
    skin_thickness = models.FloatField()
    insulin = models.FloatField()
    bmi = models.FloatField()
    diabetes_pedigree = models.FloatField()
    age = models.IntegerField(blank=True , null=True)

class HeartDisease(models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=17,null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    gender = models.CharField( max_length=50,blank=True,choices=(('female','Female'),('male','Male')))
    old_peak = models.FloatField()
    max_heart_rate = models.FloatField()
    exercise_induces_angina = models.IntegerField(blank=True,choices=((0, 'Yes'),(1, 'No')))
    number_of_major_vessels = models.IntegerField(blank=True,choices=((0,'0'),(1,'1'),(2,'2'),(3,'3'),(4,'4')))
    type_of_chest_pain = models.IntegerField(blank=True,choices=((0, 'typical angina'),(1, 'atypical angina'),(2, 'non-anginal pain'),(3, 'asymptomatic')))
    thal = models.IntegerField(blank=True,choices=((1,'1'),(2,'2'),(3,'3')))
    age = models.IntegerField(blank=True , null=True)

# Create your models here.
