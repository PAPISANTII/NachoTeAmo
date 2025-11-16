import json
from channels.generic.websocket import AsyncWebsocketConsumer

class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_id = f'game_{self.room_id}'
        
        await self.channel_layer.group_add(
            self.room_group_id,
            self.channel_name
        )
        
        await self.accept()
        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_id,
            self.channel_name
        )
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.room_group_id,
            {
                'type': 'game_message',
                'message': data['message']
            }
        )
    
    async def game_message(self, event):
        message = event['message']
        
        await self.send(text_data=json.dumps({
            'message': message
        }))