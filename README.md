# Raspberry_Pi5_Bachelor_Thesis_TormiTeedemaa
#Käesolev repositoorium sai loodud Tormi Teedemaa Bakalaureuse töö raames.<br />
########################################################### <br />
#Alljärgnevad terminali käsud võivad aidata installeerimsprotsessidele kaasa, kõik terminali käsud võtan läbi ühe sensori kaupa.<br />

#####SENSE-HAT ##### <br />
~ $ sudo nano /boot/firmware/config.txt -> kerida täiesti alla ning lisada koodirida <br />
dtoverlay=rpi-sense <br />
<br />
<br />
#####Raspberry Pi Camera ###### <br />
~ $ libcamera-hello <br />
~ $ libcamera-jpeg -o test.jpg <br />
~ $ libcamera-vid -t 10000 -o test.h264 <br /><br />

Kui jooksutada libcamera-hello ning tuleb error „no camera detected“ tuleb terminalis avada config.txt fail.<br />
~ $ sudo nano/boot/firmware/config.txt <br />
Ning lisada sinna koodirida, ning seejärel teha taaskäivitus <br />
camera_auto_detect=1 <br />
<br />
<br />
#####DHT11 ##### <br />
~ $ sudo apt install python3.11-venv <br />
~ $ python -m venv env --system-site-packages <br />
~ $ source env/bin/activate <br />

~ $ pip3 install --upgrade adafruit-python-shell <br />
~ $ pip3 install adafruit-circuitpython-dht <br />

##Peale teekide installimist tuleb teha taaskäivitus ning seejärel uuesti aktiveerida virtuaalkeskkond terminalis <br />
Kui keskkond on aktiveeritud tuleb root kausta luua DHT-Sensori kaust, kuhu lähevad DHT11 programmid.  <br />
Seejärel saab Thonnys programmeerida ülaltoodud esimese lingi abil kood. <br />
Seejärel avada uuesti terminal, veenduda, et virtuaalkeskkond on aktiivne (kasutajanime ees peab sulgudes olema „(env)“)  <br />
seejärel liikuda enda kausta, kus on DHT koodid ning käivitada need läbi terminali alljärgneva käsuga.## <br />

~ $ python3 sinukoodinimi.py <br />
#####ADC-mooduli ühendamine Raspberryga#####<br />
~ $ sudo pip3 install adafruit-circuitpython-ads1x15<br />








