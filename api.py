from fastapi import FastAPI, Path, WebSocket, WebSocketDisconnect
from pydantic import BaseModel

app = FastAPI()

class Container(BaseModel):
    container_id: int
    container_name: str
    container_blocks: int

# You should fetch information about containers from the database or elsewhere
DUMMY_CONTAINERS = [
    Container(container_id=1, container_name="container1", container_blocks=1),
    Container(container_id=2, container_name="container2", container_blocks=2),
    Container(container_id=3, container_name="container3", container_blocks=3)
]

class Sensor(BaseModel):
    sensor_id: int
    sensor_name: str
    sensor_value: int

class RobotState(BaseModel):
    containers: list[Container]
    sensors: dict[int,Sensor]
    logged: bool
    user: str
    mode: str
    block: int
    working: bool
    belt_running: bool
    photo_url: str

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
    photo_url="https://picsum.photos/200/300"
)

# Get robot state
@app.get("/state")
async def get_state():
    return robot_state

# Login user
@app.get("/login")
async def get_login(user: str, password: str):
    # Implement login
    robot_state.logged = True
    robot_state.user = user
    return {"message": "Endpoint to implement", "robot_state": robot_state.dict()}

# Logout user
@app.get("/logout")
async def get_logout():
    # Implement logout
    robot_state.logged = False
    robot_state.user = ""
    return {"message": "Endpoint to implement", "robot_state": robot_state.dict()}

# Implement robot move orders
@app.get("/movetrajectory/{move_id}")
async def get_move_trajectory(move_id: int = Path(..., gt=-1, le=4)):
    # Implement robot move orders
    return {"message": "Endpoint to implement"}
