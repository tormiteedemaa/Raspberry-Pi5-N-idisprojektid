from gpiozero import DistanceSensor
from time import sleep

#Ultrasonic sensori viigud, mis ühenduvad GPIO viikudesse
TRIG = 22
ECHO = 27

#Initsialiseeri kaugusmõõtmise sensori objekt
sensor = DistanceSensor(echo=ECHO, trigger=TRIG)

try:
    while True:
        #Mõõda distants ja arvuti sentimeetritesse
        kaugus = sensor.distance * 100
        print("Distance: " + str(round(kaugus, 2)) + " cm")
        sleep(1)

except KeyboardInterrupt:
    pass
