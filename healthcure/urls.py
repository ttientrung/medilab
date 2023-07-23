from django.urls import path
from . import views

app_name = 'healthcure'
urlpatterns = [
    path('breast-cancer/', views.breastcancer, name = "breast-cancer"),
    path('resultbc/', views.resultbc, name='resultbc'),
    path('diabetes/', views.diabetes, name = "diabetes"),
    path('resultd/', views.resultd, name='resultd'),
    path('heart-disease/', views.heartdisease, name = "heart-disease"),
    path('resulth/', views.resulth, name='resulth'),
]
