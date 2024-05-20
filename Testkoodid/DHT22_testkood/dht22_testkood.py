import time
import board
import adafruit_dht

#DHT GPIO viigu määramine
dht22 = adafruit_dht.DHT22(board.D4)

while True:
    try:
        #Võta dht pealt tulevad andmed ja väljasta need kasutajale
        temperatuur = dht22.temperature
        ohuniiskus = dht22.humidity
        print("Temperatuur: " + temperatuur)
        print("Ohuniiskus: " + ohuniiskus)
    except RuntimeError as error:
        #Kuna dht andmete lugemine võib anda erroreid, kuna mooduli lugemine pole alati edukas siis ignoreerida ühte eksimust
        print(error.args[0])
        time.sleep(2.0)
        continue
    time.sleep(2.0)