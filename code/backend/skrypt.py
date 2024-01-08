from time import sleep
from adafruit_servokit import ServoKit
import Robot_code
import asyncio
import connection

send_state_to_clients = connection.send_state_to_clients
robot_state = Robot_code.RobotCode.robot_state

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=8)

def move_to_take():

    kit.servo[1].angle = 120
    sleep(1)
    kit.servo[0].angle =80
    sleep(1)
    for i in range(180):
        if i < 103:  
            kit.servo[1].angle = 120-i  # 18
            sleep(0.01)
        if i < 64:  
            kit.servo[2].angle = 150-2*i  
            sleep(0.01) 
    sleep(1)
    take_close()
    sleep(1)
    for i in range(180):
        if i < 32:  
            kit.servo[1].angle = 18+i  #50
            sleep(0.01)
    # kit.servo[0].angle = 80
    # sleep(1)
    # kit.servo[2].angle =75
    # sleep(1)
    # kit.servo[1].angle =45
    # sleep(1)

    
def move_to_home(pos):
        
    kit.servo[1].angle =120
    sleep(1)
    kit.servo[2].angle =150
    sleep(1)

    if pos < 80:
        for i in range(180):
            if i < 80-pos:  
                kit.servo[0].angle = pos+i  
                sleep(0.01)

    if pos > 80:
        for i in range(180):
            if i < pos-80:  
                kit.servo[0].angle = pos-i  
                sleep(0.01)

    if pos == 80:
        kit.servo[0].angle = 80

def move_to_basket1():

    for i in range(180):
        if i < 80:
            kit.servo[0].angle = 75+i
            sleep(0.01)

    for i in range(180):
        if i < 10:  
            kit.servo[1].angle = 50-i  
            sleep(0.01)
        if i < 46:  
            kit.servo[2].angle = 24+i  
            sleep(0.01) 

def move_to_basket2():


    for i in range(180):
        if i < 105:
            kit.servo[0].angle = 75+i
            sleep(0.01)
    for i in range(180):
        if i < 20:  
            kit.servo[1].angle = 50+i  
            sleep(0.01)
        if i < 86:  
            kit.servo[2].angle = 24+i  
            sleep(0.01) 

def move_to_basket3():

    for i in range(180):
        if i < 70:  
            kit.servo[1].angle = 50+i  
            sleep(0.01)
        if i < 126:  
            kit.servo[2].angle = 24+i  
            sleep(0.01) 

    for i in range(180):
        if i < 75:
            kit.servo[0].angle = 80-i
            sleep(0.01)

    for i in range(180):
        if i < 70:  
            kit.servo[1].angle = 120-i  
            sleep(0.01)
        if i < 65:  
            kit.servo[2].angle = 150-i  
            sleep(0.01) 

def take_open(): # 0 zamkniete 120 otwarte
    kit.servo[3].angle =120
    sleep(1)

def take_close(): # 0 zamkniete 120 otwarte
    kit.servo[3].angle =55
    sleep(1)

def push_block():
    kit.servo[5].angle =140
    sleep(1)
    kit.servo[5].angle =55
    sleep(1)
    kit.servo[5].angle =140


def tr1():
    robot_state.robort_working = True
    asyncio.run(send_state_to_clients(robot_state)) #aktualizacja 
    move_to_take()
    robot_state.box_on_belt = False
    asyncio.run(send_state_to_clients(robot_state)) #aktualizacja
    move_to_basket1()
    sleep(1)
    take_open()
    move_to_home(155)
    robot_state.robort_working = False
    asyncio.run(send_state_to_clients(robot_state)) #aktualizacja 

def tr2():
    robot_state.robort_working = True
    asyncio.run(send_state_to_clients(robot_state)) #aktualizacja 
    move_to_take()
    robot_state.box_on_belt = False
    asyncio.run(send_state_to_clients(robot_state)) #aktualizacja
    move_to_basket2()
    sleep(1)
    take_open()
    move_to_home(180)
    robot_state.robort_working = False
    asyncio.run(send_state_to_clients(robot_state)) #aktualizacja 

def tr3():
    robot_state.robort_working = True
    asyncio.run(send_state_to_clients(robot_state)) #aktualizacja 
    move_to_take()
    robot_state.box_on_belt = False
    asyncio.run(send_state_to_clients(robot_state)) #aktualizacja
    move_to_basket3()
    sleep(1)
    take_open()
    move_to_home(0)
    robot_state.robort_working = False
    asyncio.run(send_state_to_clients(robot_state)) #aktualizacja 



# kit.servo[1].angle =120
# sleep(1)
# kit.servo[2].angle =150
# sleep(1)
# kit.servo[0].angle =80
# sleep(1)
# while True:
#     przeglob = input("Wprowadz nr serwa: ")
#     kat = input("Wprowadz liczbe: ")
#     kat = int(kat)
#     if przeglob == "1":
#         kit.servo[0].angle =kat
#         sleep(1)
#     if przeglob == "2":
#         kit.servo[1].angle =kat
#         sleep(1)
#     if przeglob == "3":
#         kit.servo[2].angle =kat
#         sleep(1)

# move_to_take()
# sleep(2)
# move_to_home(80)