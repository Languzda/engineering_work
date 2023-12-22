from fastapi import WebSocket
import asyncio
import json

class Connection:
    con_ws:set[WebSocket] = set()

    def __init__(self):    
        self.con_ws:set[WebSocket] = set()

    def add(self,websocket: WebSocket):
        self.con_ws.add(websocket)

    def remove(self,websocket: WebSocket):
        self.con_ws.remove(websocket)

connected_clients = Connection()

async def send_state_to_clients(robot_state):
    if connected_clients:
        update_message = {"event": "update", "data": robot_state.model_dump()}
        update_message_str = json.dumps(update_message)
        await asyncio.gather(*(client.send_text(update_message_str) for client in connected_clients.con_ws))
