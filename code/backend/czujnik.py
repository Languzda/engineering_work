from gpiozero import DigitalInputDevice
import time

def czunik_kamery(pin_r):
    pin = pin_r
    sensor = DigitalInputDevice(pin)
    pin_value = sensor.value
    return pin_value




        