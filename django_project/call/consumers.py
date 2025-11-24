import json
from channels.generic.websocket import AsyncWebsocketConsumer
class CallConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    async def disconnect(self, code):
        pass
    async def receive(self, text_data):
        data = json.loads(text_data)
        # Relay the signal to other peers connected to same channel group (simple echo for demo)
        # In a real app you'd route messages to intended peer
        await self.send(text_data=json.dumps({'type': data.get('type'),'data':data.get('data')}))
