from gpiozero import LED
import time

led_punane = LED(21)
led_sinine = LED(20)
def punane_polema():
    led_punane.on()
    print('LED turned on...')
def punane_kustu():
    led_punane.off()
    print('LED turned off...')
def sinine_polema():
    led_sinine.on()
    print('LED turned on...')
def sinine_kustu():
    led_sinine.off()
    print('LED turned off...')

while True:
    punane_polema()
    time.sleep(1)
    punane_kustu()
    time.sleep(1)
    sinine_polema()
    time.sleep(1)
    sinine_kustu()
    time.sleep(1)