from picamera2 import Picamera2, Preview
from gpiozero import MotionSensor
import time
#Loon ja alustan kaamera 
kaamera = Picamera2()
kaamera.start()

#Lisan pir sensori Pin-i, GPIO17, kuhu on ühendatud pir sensori signaali viik
pir = MotionSensor(17)
time.sleep(5)
print("Programm alustab tootamist")
pildi_number = 0
#Kui liikumine tuvastatud siis tee kaameraga pilt, pildi nummerdamine algab 0-st
def liikumine_tuvastatud():
    global pildi_number
    print("Liikumine tuvastatud")
    kaamera.capture_file("piltNR%s.jpg" % pildi_number)
    pildi_number += 1
    
def liikumist_pole():
    print("Liikumine peatatud")

while True:
    pir.when_motion = liikumine_tuvastatud()
    pir.when_no_motion = liikumist_pole()
    time.sleep(3)
