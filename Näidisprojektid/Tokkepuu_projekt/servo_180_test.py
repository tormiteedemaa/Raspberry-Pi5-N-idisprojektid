from gpiozero import Servo
import time

#Initsialiseeri servo
servo = Servo(13)

#Servo positsioonid saavad olla ainult vahemikus -1 kuni 1
keskel = 0
vasakule = 1 
paremale = -1
#Servo liigutamise funktsioon
def liiguta_servot(positsioon):
    servo.value = positsioon
    time.sleep(1) 

try:
    print("Servo keskel")
    liiguta_servot(keskel)
    time.sleep(2)

    print("Servo vasakule")
    liiguta_servot(vasakule)
    time.sleep(2)

    print("Servo keskele tagasi")
    liiguta_servot(keskel)
    time.sleep(2) 
    
    print("Servo paremale")
    liiguta_servot(paremale)
    time.sleep(2)

except KeyboardInterrupt:
    print("Programmi too segatud")
