from models import Sensor,RobotState,Container

class RobotCode: 
    robot_state = RobotState(
    containers = [
        Container(container_id=1, container_name="white_container", container_blocks=0), #white box #Dziala
        Container(container_id=2, container_name="red_container", container_blocks=0), #red box #Dziala
        Container(container_id=3, container_name="blue_container", container_blocks=0)  #blue box #Dziala
        ],
        sensors={
            "sensor1" : Sensor(sensor_id=1, sensor_name="sensor kamery", sensor_value=0), #camera sensor #Dziala
            "sensor2": Sensor(sensor_id=2, sensor_name="bialy sensor", sensor_value=0),  #white box sensor #Dziala
            "sensor3": Sensor(sensor_id=3, sensor_name="czerwony sensor", sensor_value=0),  #red box sensor #Dziala
            "sensor4": Sensor(sensor_id=4, sensor_name="niebieski sensor", sensor_value=0)   #blue box sensor #Dziala
        },
        logged=False,
        user="",
        mode="manual",
        block=0,
        working=False, #Dziala
        belt_running=False, #Dziala
        robort_working=False, #Dziala
        box_on_belt=False, #Dziala
        prediction=False, #Dziala
        photo_url="https://picsum.photos/200/300" #Dziala
    ) 