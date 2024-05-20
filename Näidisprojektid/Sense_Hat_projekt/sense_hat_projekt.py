from sense_hat import SenseHat
import time
import sys

#Sensehati initsialiseerimine
sense = SenseHat()
sense.clear()

#RGB varvide vaartused
sinine = (0, 0, 255) 
roheline = (0, 255, 0)   
lilla = (128, 0, 128)
punane = (255,0,0)

def temperatuur():
    temperatuur = sense.get_temperature()
    sense.show_message(f"Temp: {temperatuur:.1f}C", text_colour = sinine)

def niiskus():
    niiskus = sense.get_humidity()
    sense.show_message(f"Ohuniiskus: {niiskus:.1f}%", text_colour = roheline)
    
def nimi():
    sense.show_message("TORMI", text_colour = lilla)
    
def programmi_exit():
    sense.show_message("Goodbye", text_colour = punane)
    sense.clear()  
    sys.exit(0)    
    
while True:
    for nupuvajutus in sense.stick.get_events():
        if nupuvajutus.direction == 'up':
            temperatuur()
            time.sleep(2)
        elif nupuvajutus.direction == 'down':
            niiskus()
            time.sleep(2)
        elif nupuvajutus.direction == 'left':
            nimi()
            time.sleep(2)
        elif nupuvajutus.direction == 'right':
            programmi_exit()
            time.sleep(2)