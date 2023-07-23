from django import forms
from .models import BreastCancer, Diabetes, HeartDisease
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    r"((\([0-9]{3}\)[0-9]{9,15})|([0-9]{10,15}))", "Your number must be (xxx)xxxxxxxxx or 0xxxxxxxxx!"
)


class BreastCancerForm(forms.ModelForm):
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'firstname',
        'id': 'firstname',
        'class': 'form-control',
        'required': 'True'}))
    
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'lastname',
        'id': 'lastname',
        'class': 'form-control',
        'required': 'True'}))
    
    phone_number = forms.CharField(max_length=20, validators=[phone_validator], widget=forms.TextInput(attrs={
        'type': 'number',
        'name': 'phone',
        'id': 'phone',
        'class': "form-control",
        'required': 'True',
        'pattern': "((\([0-9]{3}\)[0-9]{9,15})|([0-9]{10,15}))",
        'title': "Your phone number must be (xxx)xxxxxxxxx or 0xxxxxxxxx"
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'type': 'email',
        'name': 'email',
        'id': 'email',
        'class': "form-control",
        'required': 'True',
    }))

    gender = forms.ChoiceField(choices=[('female','Female'),('male','Male')], widget=forms.Select(attrs={
        'name': 'gender',
        'id': 'gender',
        'class': 'form-control',
        'required': 'True'}))
    
    age = forms.IntegerField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'name': 'age',
        'id': 'age',
        'class': "form-control",
        'required': 'True',
    }))

    concave_points_mean = forms.FloatField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'step': 'any',
        'name': 'concave_points_mean',
        'id': 'concave_points_mean',
        'class': "form-control",
        'required': 'True',
    }))

    area_mean = forms.FloatField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'step': 'any',
        'name': 'area_mean',
        'id': 'area_mean',
        'class': "form-control",
        'required': 'True',
    }))

    radius_mean = forms.FloatField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'step': 'any',
        'name': 'radius_mean',
        'id': 'radius_mean',
        'class': "form-control",
        'required': 'True',
    }))

    perimeter_mean = forms.FloatField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'step': 'any',
        'name': 'perimeter_mean',
        'id': 'perimeter_mean',
        'class': "form-control",
        'required': 'True',
    }))

    concavity_mean = forms.FloatField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'step': 'any',
        'name': 'concavity_mean',
        'id': 'concavity_mean',
        'class': "form-control",
        'required': 'True',
    }))


    class Meta:
        model = BreastCancer
        fields = '__all__'


class DiabetesForm(forms.ModelForm):
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'firstname',
        'id': 'firstname',
        'class': 'form-control',
        'required': 'True'}))
    
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'lastname',
        'id': 'lastname',
        'class': 'form-control',
        'required': 'True'}))
    
    phone_number = forms.CharField(max_length=20, validators=[phone_validator], widget=forms.TextInput(attrs={
        'type': 'number',
        'name': 'phone',
        'id': 'phone',
        'class': "form-control",
        'required': 'True',
        'pattern': "((\([0-9]{3}\)[0-9]{9,15})|([0-9]{10,15}))",
        'title': "Your phone number must be (xxx)xxxxxxxxx or 0xxxxxxxxx"
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'type': 'email',
        'name': 'email',
        'id': 'email',
        'class': "form-control",
        'required': 'True',
    }))

    gender = forms.ChoiceField(choices=[('female','Female'),('male','Male')], widget=forms.Select(attrs={
        'name': 'gender',
        'id': 'gender',
        'class': 'form-control',
        'required': 'True'}))
    

    number_of_pregnancies = forms.FloatField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'name': 'number_of_pregnancies',
        'id': 'number_of_pregnancies',
        'class': "form-control",
        'required': 'True',
    }))

    glucose_conc = forms.FloatField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'name': 'glucose_conc',
        'id': 'glucose_conc',
        'class': "form-control",
        'required': 'True',
    }))

    blood_pressure = forms.FloatField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'name': 'blood_pressure',
        'id': 'blood_pressure',
        'class': "form-control",
        'required': 'True',
    }))

    skin_thickness = forms.FloatField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'name': 'skin_thickness',
        'id': 'skin_thickness',
        'class': "form-control",
        'required': 'True',
    }))

    insulin = forms.FloatField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'name': 'insulin',
        'id': 'insulin',
        'class': "form-control",
        'required': 'True',
    }))

    bmi = forms.FloatField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'step': 'any',
        'name': 'bmi',
        'id': 'bmi',
        'class': "form-control",
        'required': 'True',
    }))

    diabetes_pedigree = forms.FloatField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'step': 'any',
        'name': 'diabetes_pedigree',
        'id': 'diabetes_pedigree',
        'class': "form-control",
        'required': 'True',
    }))

    age = forms.IntegerField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'name': 'age',
        'id': 'age',
        'class': "form-control",
        'required': 'True',
    }))


    class Meta:
        model = Diabetes
        fields = '__all__'


class HeartDiseaseForm(forms.ModelForm):
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'firstname',
        'id': 'firstname',
        'class': 'form-control',
        'required': 'True'}))
    
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'lastname',
        'id': 'lastname',
        'class': 'form-control',
        'required': 'True'}))
    
    phone_number = forms.CharField(max_length=20, validators=[phone_validator], widget=forms.TextInput(attrs={
        'type': 'number',
        'name': 'phone',
        'id': 'phone',
        'class': "form-control",
        'required': 'True',
        'pattern': "((\([0-9]{3}\)[0-9]{9,15})|([0-9]{10,15}))",
        'title': "Your phone number must be (xxx)xxxxxxxxx or 0xxxxxxxxx"
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'type': 'email',
        'name': 'email',
        'id': 'email',
        'class': "form-control",
        'required': 'True',
    }))

    gender = forms.ChoiceField(choices=[('female','Female'),('male','Male')], widget=forms.Select(attrs={
        'name': 'gender',
        'id': 'gender',
        'class': 'form-control',
        'required': 'True'}))

    old_peak = forms.FloatField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'step': 'any',
        'name': 'op',
        'id': 'op',
        'class': "form-control",
        'required': 'True',
    }))

    max_heart_rate = forms.FloatField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'step': 'any',
        'name': 'mhra',
        'id': 'mhra',
        'class': "form-control",
        'required': 'True',
    }))

    exercise_induces_angina = forms.ChoiceField(choices=[(0, 'Yes'),(1, 'No')], widget=forms.Select(attrs={
        'name': 'eia',
        'id': 'eia',
        'class': 'form-control',
        'required': 'True'}))
    
    number_of_major_vessels = forms.ChoiceField(choices=[(0,'0'),(1,'1'),(2,'2'),(3,'3'),(4,'4')], widget=forms.Select(attrs={
        'name': 'nmv',
        'id': 'nmv',
        'class': 'form-control',
        'required': 'True'}))
    
    type_of_chest_pain = forms.ChoiceField(choices=[(0, 'typical angina'),(1, 'atypical angina'),(2, 'non-anginal pain'),(3, 'asymptomatic')], widget=forms.Select(attrs={
        'name': 'tcp',
        'id': 'tcp',
        'class': 'form-control',
        'required': 'True'}))

    age = forms.IntegerField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'name': 'age',
        'id': 'age',
        'class': "form-control",
        'required': 'True',
    }))

    thal = forms.ChoiceField(choices=[(1,'1'),(2,'2'),(3,'3')], widget=forms.Select(attrs={
        'name': 'thal',
        'id': 'thal',
        'class': 'form-control',
        'required': 'True'}))

    class Meta:
        model = HeartDisease
        fields = '__all__'