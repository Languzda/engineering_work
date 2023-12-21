from gpiozero import OutputDevice
from time import sleep
from adafruit_servokit import ServoKit
#####
import Robot_code
import connection
import asyncio

kit = ServoKit(channels=8)
gpio_pin = OutputDevice(26)
servo_index = 7

robot_state = Robot_code.RobotCode.robot_state
send_state_to_clients = connection.send_state_to_clients

def start():
    try:
        gpio_pin.on()
        kit.continuous_servo[servo_index].throttle = 1
        robot_state.belt_running = True
        asyncio.run(send_state_to_clients(robot_state)) #aktualizacja 
        return True

    except Exception as e:
        print(f"An exception occurred: {e}")
    
async def stop():
    try:
        robot_state.working = False
        await send_state_to_clients(robot_state)

        print("Zatrzymywanie robota...")
        gpio_pin.off()
        kit.continuous_servo[servo_index].throttle = 0  
    except Exception as e:
        print(f"An exception occurred: {e}")
    finally:
        gpio_pin.close()


def wait(): 
    try:
        gpio_pin.off()
        kit.continuous_servo[servo_index].throttle = 0
        robot_state.belt_running = False
        asyncio.run(send_state_to_clients(robot_state)) #aktualizacja   
    except Exception as e:
        print(f"An exception occurred: {e}")


