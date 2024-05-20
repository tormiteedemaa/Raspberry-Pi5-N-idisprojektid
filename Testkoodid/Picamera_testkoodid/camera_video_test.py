from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
import time

#Määrame kaamera ja video tegemiseks vajalikud muutujad,enkooderi väärtuse ja väljundi nime
kaamera = Picamera2()
video_konfiguratsioon = kaamera.create_video_configuration()
kaamera.configure(video_konfiguratsioon)
enkooder = H264Encoder(100000000)
valjund = FfmpegOutput('testvideo.mp4')

kaamera.start_preview(Preview.QTGL)

#Filmi 5 sekundit ja salvesta video valjund muutujasse
kaamera.start_recording(enkooder, valjund)
time.sleep(5)
kaamera.stop_recording()
kaamera.close()
