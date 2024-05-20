from picamera2 import Picamera2, Preview

#Initsialiseerin kaamera
picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)
picam2.start()
#Tee testpilt
picam2.capture_file("testpilt.jpg")