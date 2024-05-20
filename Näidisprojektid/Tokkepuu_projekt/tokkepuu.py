from gpiozero import DistanceSensor, LED, TonalBuzzer
from gpiozero.tones import Tone
import time
from gpiozero import PWMOutputDevice

# Defineerin GPIO pin-id ja initsialiseerin sensorid
trigger = 22
echo = 27
led_punane = LED(21)
led_sinine = LED(20)
sagedus = 220 #Hz
servo = PWMOutputDevice(13, frequency=50)
#Ultraheli mooduli initsialiseerimine
ultraheli_sensor = DistanceSensor(echo=echo, trigger=trigger)

#Impulsi loomise funktsioon servo keeramise jaoks
def impulss(impulsi_laius):
    tootsukkel = impulsi_laius / 20.0
    servo.value = tootsukkel
    time.sleep(1)  
def rongi_sireen():
    helikolar = TonalBuzzer(19)
    helikolar.play(Tone(sagedus))
    time.sleep(2)
    helikolar.close() 
    time.sleep(1)  
def tokkepuu_alla():
    impulss(0.5)
def tokkepuu_ulesse():
    impulss(1.5)
    
#Põhifunktsioon, mis töötab lõpmatuseni või klaviatuuri katkestuseni
def main():
    madal = False #muutuja, et jälgida, mis seisus on tõkkepuu
    try:
        while True:
            tokkepuu_ulesse()
            kaugus = ultraheli_sensor.distance * 100  #Kaugus tuleb teisendada sentimeetritesse
            print("Objekti kaugus: " + str(round(kaugus, 2)) + " cm")
            
            if kaugus < 10 and madal == False:  
                madal = True
                led_sinine.off()
                rongi_sireen()
                tokkepuu_alla()
                rongi_sireen()
                while kaugus < 10 and madal == True:
                    led_punane.on()
                    time.sleep(0.5)
                    led_punane.off()
                    time.sleep(0.5)
                    kaugus = ultraheli_sensor.distance *100
                    print("Objekti kaugus: " + str(round(kaugus, 2)) + " cm")
            elif kaugus > 10 and madal == True: 
                tokkepuu_ulesse()
                time.sleep(1)
                led_punane.off()
                led_sinine.on()
                madal = False
            elif kaugus > 10 and madal == False:  
                led_sinine.on()
                time.sleep(1)
    except KeyboardInterrupt:
        #Kustuta ledid ja tõsta tõkkepuu ülesse
        tokkepuu_ulesse()
        led_punane.off()
        led_sinine.off()

#Jooksutab põhifunktsiooni
if __name__ == "__main__":
    main()

    


    
    