from fastapi import WebSocket

class Connection:

    def __init__(self):    
        self.con_ws:set[WebSocket] = set()

    def add(self,websocket: WebSocket):
        self.con_ws.add(websocket)

    def remove(self,websocket: WebSocket):
        self.con_ws.remove(websocket)

connected_clients = Connection()
