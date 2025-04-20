import json
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class DoctorConsumer(WebsocketConsumer):
    def connect(self):
        self.doctor_id = self.scope['user'].doctorprofile.id
        self.group_name = f'doctor_{self.doctor_id}'

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()
        self.send(text_data=json.dumps({'message': 'Connected to Doctor Dashboard'}))

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def send_new_appointment(self, event):
        appointment_html = event['appointment']

        self.send(text_data=json.dumps({
            'type': 'new_appointment',
            'appointment': appointment_html,
        }))
