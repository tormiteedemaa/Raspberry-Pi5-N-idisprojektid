from picamera2 import Picamera2, Preview
import time

#Initsialiseerin fotode tegemiseks kaamera
kaamera = Picamera2()
kaamera.start_preview(Preview.QTGL)
kaamera.start()
#Tee 5 pilti, tee üks pilt iga viie sekundi tagant
for i in range(5):
    kaamera.capture_file("image%s.jpg" % i)
    time.sleep(5)

#Väljasta kasutajale et pildid on tehtud ja sulge kaamera
print('Pildid tehtud')
kaamera.close()
    