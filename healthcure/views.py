from django.shortcuts import render, redirect
from .models import BreastCancer, Diabetes, HeartDisease
from medilab.models import *
from .forms import BreastCancerForm, DiabetesForm, HeartDiseaseForm
import cv2
import pickle
import imutils
import sklearn
from tensorflow.keras.models import load_model
import joblib
import numpy as np

breastcancer_model = joblib.load('models/breast_cancer_model.pkl')
diabetes_model = pickle.load(open('models/diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('models/heart_disease_model.dat', 'rb'))

def index(request):
    context = {}
    return render(request, 'index.html', context)

def homepage(request):
    departments = Department.objects.all()
    context = {'departments': departments}
    print(departments)
    return render(request, 'homepage.html', context)

def breastcancer(request):
    page = 'healthcure'
    form = BreastCancerForm()
    context = {'form': form, 'page': page}
    return render(request, 'healthcure/breastcancer.html', context)

def resultbc(request):
    page = 'healthcure'
    if request.method == 'POST':
        form = BreastCancerForm(request.POST, BreastCancer)
        # print(form.errors)
        if form.is_valid():
            form.save()
            firstname = request.POST.get('first_name')
            lastname = request.POST.get('last_name')
            gender = request.POST.get('gender')
            age = request.POST.get('age')
            cpm = request.POST.get('concave_points_mean')
            am = request.POST.get('area_mean')
            rm = request.POST.get('radius_mean')
            pm = request.POST.get('perimeter_mean')
            cm = request.POST.get('concavity_mean')
            pred = breastcancer_model.predict(np.array([cpm, am, rm, pm, cm]).reshape(1, -1))

    context = {'firstname': firstname, 'lastname': lastname, 'gender': gender, 'age': age, 'pred': pred, 'page': page}
    return render(request, 'healthcure/resultbc.html', context)

def diabetes(request):
    page = 'healthcure'
    form = DiabetesForm()
    context = {'form': form, 'page': page}
    return render(request, 'healthcure/diabetes.html', context)

def resultd(request):
    page = 'healthcure'
    if request.method == 'POST':
        form = DiabetesForm(request.POST, Diabetes)
        print(form.errors)
        if form.is_valid():
            form.save()
            firstname = request.POST.get('first_name')
            lastname = request.POST.get('last_name')
            gender = request.POST.get('gender')
            insulin = request.POST.get('insulin')
            bmi = request.POST.get('bmi')
            diabetes_pedigree = request.POST.get('diabetes_pedigree')
            age = request.POST.get('age')
            print(gender)
            pred = diabetes_model.predict([[insulin, bmi, diabetes_pedigree, age]])
        
    context = {'firstname': firstname, 'lastname': lastname, 'gender': gender, 'age': age, 'pred': pred, 'page': page}
    return render(request, 'healthcure/resultd.html', context)

def heartdisease(request):
    page = 'healthcure'
    form = HeartDiseaseForm()
    context = {'form': form, 'page': page}
    return render(request, 'healthcure/heartdisease.html', context)

def resulth(request):
    page = 'healthcure'
    if request.method == 'POST':
        form = HeartDiseaseForm(request.POST, HeartDisease)
        print(form.errors)
        if form.is_valid():
            form.save()
            firstname = request.POST.get('first_name')
            lastname = request.POST.get('last_name')
            gender = request.POST.get('gender')
            old_peak = float(request.POST.get('old_peak'))
            exercise_induces_angina = int(request.POST.get('exercise_induces_angina'))
            number_of_major_vessels = int(request.POST.get('number_of_major_vessels'))
            type_of_chest_pain = int(request.POST.get('type_of_chest_pain'))
            thal = int(request.POST.get('thal'))
            age = int(request.POST.get('age'))
            max_heart_rate = float(request.POST.get('max_heart_rate'))
            print(type(number_of_major_vessels), type(type_of_chest_pain), type(exercise_induces_angina), type(thal), type(old_peak), type(max_heart_rate), type(age))
            pred = heart_model.predict(np.array([number_of_major_vessels, type_of_chest_pain, exercise_induces_angina, thal, old_peak, max_heart_rate, age]).reshape(1, -1))
        
    context = {'firstname': firstname, 'lastname': lastname, 'gender': gender, 'age': age, 'pred': pred, 'page': page}
    return render(request, 'healthcure/resulth.html', context)
# Create your views here.
