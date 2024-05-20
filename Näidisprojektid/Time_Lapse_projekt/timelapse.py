import cv2
import time

#Kestvusaeg ja intervall
kestvusaeg = 3600
intervall = 5
#Kaadrite koguarv
kaadrid = kestvusaeg // intervall

#Alustan kaamera
cap = cv2.VideoCapture(0)

for i in range(kaadrid):
    #Kaadri sisselugemine
    ret, img = cap.read()

    # Salvestan kaadri pildifailina
    failinimi = f"pilt_nr_{i:d}.png"
    cv2.imwrite(failinimi, img)

    # Ootan intervalli aja
    time.sleep(intervall)

#Vabastan kaamera peale programmi loppu
cap.release()
cv2.destroyAllWindows()