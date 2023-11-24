
from channels.generic.websocket import AsyncWebsocketConsumer
from django.template import Context, Template
import json 

class SQLBrokerExecConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        # Add this consumer to the group
        await self.channel_layer.group_add(
            "asynch_sql",
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, close_code):
        # Remove this consumer from the group when it disconnects
        await self.channel_layer.group_discard(
            "asynch_sql",
            self.channel_name
        )

    async def receive(self, text_data):
        # text_data contains the message from the client
        print(f"Message received: {text_data}")

        # You can send a message back to the client
        await self.send(text_data=json.dumps({
            'message': 'Message received by the server Ohohrrrohorhoh '
        }))

    async def send_notification(self, event):
        message = event['message']
        print(f"Message sent: {message}")
        # Send the message to the client
        await self.send(text_data=json.dumps({
            'message': message
        }))