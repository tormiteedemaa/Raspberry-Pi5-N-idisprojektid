import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

#ADC konstandid
adc_maksimaalne = 65535 # Maksimaalne adc vaartus 16-bitilisega
referents_pinge = 3.3 # Referents pinge 3.3V

# Testimise teel saadud vahemik maksimaalsest ja minimaalsest vaartuste vahemikust
min_vaartus = 3200 
max_vaartus = 4500
#Minimaalse ja maksimaalse pinge arvutamine adc vaartuste pohjals
min_pinge = (min_vaartus / adc_maksimaalne) * referents_pinge
max_pinge = (max_vaartus / adc_maksimaalne) * referents_pinge

#Initsialeeri ADC 
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
adc_kanal = AnalogIn(ads, ADS.P0)

def baasvahemik(pinge):
    return min_pinge <= pinge <= max_pinge

def pingeteisendus(adc_vaartus):
    return (adc_vaartus / adc_maksimaalne) * referents_pinge

try:
    #Baasvahemiku arvutamine
    alus_pinge = (min_pinge + max_pinge) / 2
    print("Baasvahemikus:", alus_pinge)

    while True:
        adc_vaartus = adc_kanal.value  #adc vaartuse sisselugemine
        pinge = pingeteisendus(adc_vaartus)
        if baasvahemik(pinge):
            print("Baasvahemikus")
        else:
            nihe = pinge - alus_pinge
            print("Sinu hingeohus on CO2 baasvahemikust nii palju rohkem:", nihe)
        time.sleep(1)
except KeyboardInterrupt:
    pass
