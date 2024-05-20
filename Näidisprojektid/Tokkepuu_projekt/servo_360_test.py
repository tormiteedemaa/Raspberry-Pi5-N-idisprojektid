from gpiozero import Servo
import time
#Servo GPIO viik
servo = Servo(13)

#Keera servot 90 kraadi ja 3 sekundi pärast keera servot teistpidi 90 kraadi
print("Start in middle")
servo.value = 0
time.sleep(0.34)
servo.value = None
time.sleep(3)
servo.value = 0.5
time.sleep(0.31)
servo.value = None
time.sleep(0.1)