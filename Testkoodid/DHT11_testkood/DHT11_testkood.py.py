import time
import board
import adafruit_dht

# DHT GPIO viigu määramine
dht11 = adafruit_dht.DHT11(board.D4)


while True:
    try:
        #Võta dht pealt tulevad andmed ja väljasta need kasutajale
        temperatuur = dht11.temperature
        ohuniiskus = dht11.humidity
        print("Temperatuur: " + temperatuur)
        print("Ohuniiskus: " + ohuniiskus)

    except RuntimeError as error:
        #Kuna dht andmete lugemine võib anda erroreid, sest mooduli lugemine pole alati edukas siis ignoreerida ühte eksimust
        print(error.args[0])
        time.sleep(2.0)
        continue
    time.sleep(2.0)