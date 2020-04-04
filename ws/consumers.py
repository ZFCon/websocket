import json
from channels.generic.websocket import WebsocketConsumer

from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model

import asyncio

User = get_user_model()

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.channel_layer.group_add(
            "test",
            self.channel_name
        )
        # users = await self.get_users()
        await self.send(
            {
                "type": "websocket.accept",
            }
        )

    async def websocket_disconnect(self, event):
        # print('bitch')
        pass

    async def websocket_receive(self, event):
        await self.channel_layer.group_send(
            "test",
            {
                "type": "websocket.send",
                "text": event['text']
            }
        )

    # @database_sync_to_async
    # def get_users(self):
    #     return User.objects.all()

# from channels.generic.websocket import AsyncJsonWebsocketConsumer


# class NotificationConsumer(AsyncJsonWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#     async def notify(self, event):
#         await self.send_json(event["content"])


#     async def receive_json(self, content, **kwargs):
#         group_name = serializer.get_group_name()
#         self.groups.append(group_name)
#         await self.channel_layer.group_add(
#             group_name,
#             self.channel_name,
#         )