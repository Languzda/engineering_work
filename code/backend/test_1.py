import Robot_code
import connection
import time 


robot_state = Robot_code.RobotCode.robot_state
send_state_to_clients = connection.send_state_to_clients

async def start_web_socket():
    while True:
        await send_state_to_clients(robot_state)
        time.sleep(1)

