# Imports
import time
from gpiozero import MotionSensor

#define the pins
pir = MotionSensor(14)

while True:
    if pir.motion_detected:
        print("You moved")
    time.sleep(2)

