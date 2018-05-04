# Imports
import time
import datetime
from subprocess import call
from gpiozero import MotionSensor
import subprocess

#define the pins
pir = MotionSensor(14)


while True:
    if pir.motion_detected:
        now = datetime.datetime.now()
        print (str(now) + " - Movimiento detectado en el salon.")
        call(["/usr/local/bin/telegram-send", "Movimiento detectado en salon.")
    time.sleep(2)

