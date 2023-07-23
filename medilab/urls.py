from django.urls import path
from . import views

app_name = 'medilab'
urlpatterns = [
    path('', views.index, name = "index"),
    path('get_department/', views.get_department, name = "get_department"),
]
