from pydantic import BaseModel,validator, field_validator, model_validator
from Container import Container
from Sensor import Sensor
import json
import asyncio
import connection

class RobotState(BaseModel):
    containers: list[Container]
    sensors: dict[int,Sensor]
    logged: bool
    user: str
    mode: str
    block: int
    working: bool
    belt_running: bool
    robort_working: bool
    photo_url: str

    async def send_state_to_clients(self,ws_connections: set):
        if ws_connections:
            update_message = {"event": "update", "data": self.model_dump()}
            update_message_str = json.dumps(update_message)
            send=asyncio.create_task(*(client.send_text(update_message_str) for client in ws_connections))
            await send

    @model_validator(mode='after')
    async def on_update(self):
       await self.send_state_to_clients(connection.connected_clients.con_ws)
   

