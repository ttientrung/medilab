from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/doctor_dashboard/", consumers.DoctorConsumer.as_asgi()),
]