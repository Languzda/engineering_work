from fastapi import FastAPI, Path, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import Robot_code
import connection
# import test_1
import threading
import logs

########
from main import task_tasma,task_czujnik

robot_state = Robot_code.RobotCode.robot_state
logger = logs.logger
working_flag = 0

thread_tasma = threading.Thread(target=task_tasma)
thread_tasma.start()
thread_czujnik = threading.Thread(target=task_czujnik)
thread_czujnik.start()


app = FastAPI()
# Dodaj middleware do obsługi CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tutaj możesz określić dozwolone domeny
    allow_credentials=True,
    allow_methods=["*"],  # Tutaj możesz określić dozwolone metody HTTP
    allow_headers=["*"],  # Tutaj możesz określić dozwolone nagłówki
)


send_state_to_clients = connection.send_state_to_clients
send_log_to_clients = connection.send_log_to_clients

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connection.connected_clients.add(websocket)
    print("Client connected:", websocket)
    
    # Wysłanie aktualnych danych zaraz po nawiązaniu połączenia
    await send_state_to_clients(robot_state)
    
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
            # await test_1.start_web_socket()
    except WebSocketDisconnect:
        connection.connected_clients.remove(websocket)
        print("Client disconnected:", websocket)
        await send_state_to_clients(robot_state)  # Zaktualizuj wywołanie funkcji

@app.websocket("/ws/logs")
async def log_websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connection.connected_clients_log.add(websocket)
    print("Log client connected:", websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        connection.connected_clients_log.remove(websocket)
        print("Log client disconnected:", websocket)

# Get robot state
@app.get("/state")
async def get_state():
    await send_state_to_clients(robot_state)
    return {"message": "OK", "data": robot_state.model_dump()}

# Login user
@app.post("/login")
async def get_login(request_body: dict):
    user = request_body.get("user")
    password = request_body.get("password")
    # Implement login
    robot_state.logged = True
    robot_state.user = user
    await send_state_to_clients(robot_state)
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
    await send_state_to_clients(robot_state)
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
        await send_state_to_clients(robot_state)
        return {"message": "OK"}
    else:
        await send_state_to_clients(robot_state)
        return {"message": "Error: Robot is working"}

@app.get("/stop")
async def get_stop():
    print(robot_state.working)
    if robot_state.working:
        robot_state.working = False
        await send_state_to_clients(robot_state)
        return {"message": "OK_stop"}
    else:
        await send_state_to_clients(robot_state)
        return {"message": "Everything is already stopped"}

    
@app.get("/start")
async def get_start():
    print(robot_state.working)
    if robot_state.working:
        return {"message": "Everything is already working"}
    else:
        robot_state.working = True
        logger.add("info", "Robot started")
        await send_log_to_clients(logger)
        await send_state_to_clients(robot_state)
        return {"message": "OK_start"}

@app.get("/mode/{mode_id}")
async def get_mode(mode_id: int = Path(..., gt=-1, le=1)):
    if(mode_id == 0):
        robot_state.mode = "manual"
    elif(mode_id == 1):
        robot_state.mode = "auto"
    else:
        await send_state_to_clients(robot_state)
        return {"message": "Wrong mode id"}
    await send_state_to_clients(robot_state)
    return {"message": "zamiana trybu" }
