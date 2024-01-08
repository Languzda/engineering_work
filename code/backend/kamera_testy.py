import cv2
import Robot_code
import asyncio
import connection

send_state_to_clients = connection.send_state_to_clients
robot_state = Robot_code.RobotCode.robot_state

def kamera():

    cam = cv2.VideoCapture(0)
    
    try:
        ret, image = cam.read()
        if ret:
            #cv2.imshow('Image from Camera', image)
            cv2.waitKey(0) 
            img_path = '/home/Alusya/Desktop/inzynierka/robot/zdj/new.jpg'
            cv2.imwrite(img_path, image)
            robot_state.photo_url = img_path
            asyncio.run(send_state_to_clients(robot_state)) #aktualizacja 
            print("zdj zapisane")
        else:
            print("Blad")
    
    finally:
        cam.release()
        cv2.destroyAllWindows()