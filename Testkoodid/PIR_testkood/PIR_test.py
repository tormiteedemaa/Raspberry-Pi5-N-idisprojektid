from gpiozero import MotionSensor
import time

#Pir sensori ühendatud GPIO17 viiguga
pir = MotionSensor(17)

def Liikumine():
    print("Liikumine tuvastatud")

def Paigal():
    print("Liikumine peatatud")

while True: 
    pir.when_motion = Liikumine()
    pir.when_no_motion = Paigal()
    time.sleep(3)


