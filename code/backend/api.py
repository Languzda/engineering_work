from fastapi import FastAPI, Path, WebSocket, WebSocketDisconnect
import json
import asyncio
from models import RobotState, Container, Sensor
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Dodaj middleware do obsługi CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tutaj możesz określić dozwolone domeny
    allow_credentials=True,
    allow_methods=["*"],  # Tutaj możesz określić dozwolone metody HTTP
    allow_headers=["*"],  # Tutaj możesz określić dozwolone nagłówki
)

# You should fetch information about containers from the database or elsewhere
DUMMY_CONTAINERS = [
    Container(container_id=1, container_name="container1", container_blocks=1),
    Container(container_id=2, container_name="container2", container_blocks=2),
    Container(container_id=3, container_name="container3", container_blocks=3)
]

robot_state = RobotState(
    containers=DUMMY_CONTAINERS,
    sensors={
        1: Sensor(sensor_id=1, sensor_name="sensor1", sensor_value=1),
        2: Sensor(sensor_id=2, sensor_name="sensor2", sensor_value=2),
        3: Sensor(sensor_id=3, sensor_name="sensor3", sensor_value=3)
    },
    logged=False,
    user="",
    mode="manual",
    block=0,
    working=False,
    belt_running=False,
    robort_working=False,
    photo_url="https://picsum.photos/200/300"
)

connected_clients:set[WebSocket] = set()

async def send_state_to_clients():
    if connected_clients:
        update_message = {"event": "update", "data": robot_state.model_dump()}
        update_message_str = json.dumps(update_message)
        await asyncio.gather(*(client.send_text(update_message_str) for client in connected_clients))

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    print("Client connected:", websocket)
    
    # Wysłanie aktualnych danych zaraz po nawiązaniu połączenia
    await send_state_to_clients()
    
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        connected_clients.remove(websocket)
        print("Client disconnected:", websocket)
        await send_state_to_clients()  # Zaktualizuj wywołanie funkcji

# Get robot state
@app.get("/state")
async def get_state():
    await send_state_to_clients()
    return {"message": "OK", "data": robot_state.model_dump()}

# Login user
@app.get("/login")
async def get_login(user: str, password: str):
    # Implement login
    robot_state.logged = True
    robot_state.user = user
    await send_state_to_clients()
    success = True
    if(success):
        return {"message": "OK"}
    else:
        return {"message": "Wrong username or password"}

# Logout user
@app.get("/logout")
async def get_logout():
    # Implement logout
    robot_state.logged = False
    robot_state.user = ""
    await send_state_to_clients()
    success = True
    if(success):
        return {"message": "OK"}
    else:
        return {"message": "Sth went wrong"}

# Implement robot move orders
@app.get("/movetrajectory/{move_id}")
async def get_move_trajectory(move_id: int = Path(..., gt=-1, le=3)):
    # Implement robot move orders
    if(robot_state.working == False):
        # Implement robot move (wykorzystaj send_state_to_clients() po aktualizacji stanu robota)
        robot_state.block = move_id
        await send_state_to_clients()
        return {"message": "OK"}
    else:
        await send_state_to_clients()
        return {"message": "Error: Robot is working"}

@app.get("/stop")
async def get_stop():
    if(robot_state.working):
        # Implement robot stop
        robot_state.working = False
        await send_state_to_clients()
        return {"message": "OK"}
    else:
        await send_state_to_clients()
        return {"message": "Everythig is already stopped"}
    
@app.get("/start")
async def get_start():
    if(robot_state.working):
        await send_state_to_clients()
        return {"message": "Everythig is already working"}
    else:
        # Implement robot start
        robot_state.working = True
        await send_state_to_clients()
        return {"message": "OK"}

@app.get("/mode/{mode_id}")
async def get_mode(mode_id: int = Path(..., gt=-1, le=1)):
    if(mode_id == 0):
        robot_state.mode = "manual"
    elif(mode_id == 1):
        robot_state.mode = "auto"
    else:
        await send_state_to_clients()
        return {"message": "Wrong mode id"}
    await send_state_to_clients()
    return {"message": "Actual mode: " + robot_state.mode}
