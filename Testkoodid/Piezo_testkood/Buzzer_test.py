from gpiozero import Buzzer
import time

buzzer = Buzzer(19)

#Piiksumise test, mis teeb 5 piiksu ja siis lopetab programmi
for i in range(5):
    buzzer.on()
    print ("Beep")
    time.sleep(0.5)
    buzzer.off()
    print ("No Beep")
    time.sleep(0.5)