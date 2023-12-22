import czujnik
from time import sleep
from tasma import start,stop,wait
import kamera_testy
import skrypt
import predykcja
import Robot_code
import connection
import asyncio

robot_state = Robot_code.RobotCode.robot_state
send_state_to_clients = connection.send_state_to_clients


def task_tasma():
    print("Start skryptu")
    skrypt.move_to_home(75)
    while True:
        if robot_state.working == True:
            skrypt.push_block()
            robot_state.box_on_belt = True
            asyncio.run(send_state_to_clients(robot_state)) #aktualizacja
            while czujnik.czunik_kamery(pin_r=0) == 0 :
                sleep(0.1)
                success = start()
                if not success:
                    print("Error during start()")
                    break
            robot_state.sensors["sensor1"].sensor_value = 1
            asyncio.run(send_state_to_clients(robot_state)) #aktualizacja 
            sleep(0.3) 
            robot_state.sensors["sensor1"].sensor_value = 0
            asyncio.run(send_state_to_clients(robot_state)) #aktualizacja 
            wait() 
            kamera_testy.kamera()
            robot_state.prediction = True
            asyncio.run(send_state_to_clients(robot_state)) #aktualizacja 
            pred = predykcja.pred()
            robot_state.prediction = False
            asyncio.run(send_state_to_clients(robot_state)) #aktualizacja
            start()
            sleep(2.1)
            wait() 
            if pred == 0:
                skrypt.tr1()
            elif pred == 1:
                skrypt.tr2()
            elif pred == 2:
                skrypt.tr3()




def task_czujnik():
    biala =0
    czerwona = 0
    niebieski = 0
    while True:
        if robot_state.box_on_belt==False:
            if czujnik.czunik_kamery(5) == 1:
                biala = biala +1
                robot_state.sensors["sensor2"].sensor_value = 1
                asyncio.run(send_state_to_clients(robot_state)) #aktualizacja
                robot_state.containers[0].container_blocks = biala
                asyncio.run(send_state_to_clients(robot_state)) #aktualizacja 
                print(f"czerwony = {biala}")
                sleep(3)
                robot_state.sensors["sensor2"].sensor_value = 0
                asyncio.run(send_state_to_clients(robot_state)) #aktualizacja 
            if czujnik.czunik_kamery(6) == 1:
                czerwona = czerwona + 1
                robot_state.sensors["sensor3"].sensor_value = 1
                asyncio.run(send_state_to_clients(robot_state)) #aktualizacja
                robot_state.containers[1].container_blocks = czerwona
                asyncio.run(send_state_to_clients(robot_state)) #aktualizacja 
                print(f"bialy = {czerwona}")
                sleep(3)
                robot_state.sensors["sensor3"].sensor_value = 0
                asyncio.run(send_state_to_clients(robot_state)) #aktualizacja 
            if czujnik.czunik_kamery(13) == 1:
                niebieski = niebieski +1
                robot_state.sensors["sensor4"].sensor_value = 1
                robot_state.containers[2].container_blocks = niebieski
                asyncio.run(send_state_to_clients(robot_state)) #aktualizacja 
                print(f"niebieski = {niebieski}")
                sleep(3)    
                robot_state.sensors["sensor4"].sensor_value = 0
                asyncio.run(send_state_to_clients(robot_state)) #aktualizacja 





