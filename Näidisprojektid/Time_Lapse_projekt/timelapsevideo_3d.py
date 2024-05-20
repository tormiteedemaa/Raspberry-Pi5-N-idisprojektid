import cv2
import os

#Kaust, kus asuvad pildid, muuta vastavalt kasutaja konfiguratsioonile
failide_kaust = "/home/tormi/Desktop/Timelapse"

#Valjundvideo nimi
valjund_video = "timelapse_video.mp4"

#Tekitan loendi, kus asuvad koik pildid
piltide_list = sorted([f for f in os.listdir(failide_kaust) if f.lower().endswith((".jpg", ".png"))])

#Valin esimese pildi, et saada koik mootmed
esimene_pilt = cv2.imread(os.path.join(failide_kaust, piltide_list[0]))
korgus, laius, kihid = esimene_pilt.shape

#Initsialiseerin video tegemise
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  
fps = 30
out = cv2.VideoWriter(valjund_video, fourcc, fps, (laius, korgus))

#Votan iga pilt eraldi ja liidan videole juurde
for pildi_fail in piltide_list:
    pildi_tee = os.path.join(failide_kaust, pildi_fail)
    img = cv2.imread(pildi_tee)
    out.write(img)

#Vabastan videokirjutaja
out.release()

#Annan kasutajale teada, et video on valmis ja mis nime all video on olemas
print(f"Time-lapse video salvestatud nimega: {valjund_video}")
