# quadcopter
Python code for Quadcopter

I will use a rasbperry Pi V 2 or B+ in order to read sensors and write ESC controller to controll Brushless Motors.
The Copter will be 4+4 Motored with handmade chassey.

some party might be german. If you have some questions, please ask!

# First Ideas 
Multicopter mit Raspberry Pi


Ziel: Autonom fliegender Multicopter mit Nutzlast gesteuert über UMTS.

Benötigte Kompontenen:

Raspberry Pi
GPS Sensor
Gyro Sensor / Magnetfeld / Accelerator LSM9DS0
Barometischer Höhenmessung Adafruit MPL3115A2
Annäherungssensor
GSM Modem
Servo Steuerung PCA9685
4x Motor (Brushless) für Auftrieb
4x Motor (Brushless) zur Steuerung
4x ESC30A
4x ESC 20A
Akkus 22V, 11V, 5V
Propeller
LED Erweiterung TLC5947


c

80g each

http://www.premium-modellbau.de/Brushless-Regler-4x-Sunrise-30A-BLHeli-Multi-Slim-Multicopter-Brushless-Regler--2S---6S-Opto/a51213050_u2344_zf3ebed25-9a7a-4580-8f8e-0931979146bb/

20g each

http://www.premium-modellbau.de/Brushless-Motoren-4x-Emax-MT2206-Brushless-Motor-1900kv-2S-3S-32g-Mini-Multicopter-Quadcopter-Set/a50507460_u2344_zf3ebed25-9a7a-4580-8f8e-0931979146bb/

32g each

http://www.premium-modellbau.de/Brushless-Regler-4x-Sunrise-20A-BLHeli-Multi-Slim-Multicopter-Brushless-Regler-2S---6S-Opto/a51213033_u2344_zf3ebed25-9a7a-4580-8f8e-0931979146bb/

12g each
http://www.premium-modellbau.de/Quadcopter---Multicopter-Motoren-4x-Emax-MT3110-Brushless-Motor-480kv-4S-6S-78g-Quadcopter-Set/a50623737_u2344_z87d8295e-7404-4362-a97d-9fa19b304786/

249g

https://www.aerolab.de/kabel-adapter/dualsky-h-e-d-lipo-6s-6250ma-xp62506hed-xpower-battery/a-502412/
850g


4 Rotoren werden ausschließlich zur Höhenkontrolle verwendet. Ideal sollten diese mit möglichst wenig Leistung den Copter zum abheben bringen ~20%
daraus ergibt sich ein Gesammtgewicht von unter 1400g


4 kleinere Rotoren steuern den Copter

Möglichkeiten den Copter zu steuern:
klassische Drehzahländerungen an den Steuerpropellern
Drehen der Motoren um Schub umzuleiten.




AI:
Kleines Display (i2C) für Statusmeldungen
Piezo Lautsprecher für Akkustische Rückmeldung
ggf LED Rückmeldung
Servosteuerung i2c für die Ansteuerung eines ESC
Gyro auslesen i2c
Servosteuerung auf basis vom Gyro
Design des Copter
Übertrag auf 4 Rotoren (Hauptrotoren)
Remote steuerung über GSM / Wifi mittels PC
Kamerabild übertragen
Gain Steuerung der Hauptrotoren (Hover)
Pitch durch Drehmomentschiebung bei den Kontrollpropellern
Rollen und Kippen über die Achse mit den Kontrollpropellern
Steuerung über Remote
Steuerung über FixPositionen (GPS)

Nice to Have:
GUI für Remote
LED Show am Copter
zweite Kamera am Copter
Hardware schalten zum abschalten der Akkus (Sicherheitsschalter)





Videoübertragung

http://blog.miguelgrinberg.com/post/stream-video-from-the-raspberry-pi-camera-to-web-browsers-even-on-ios-and-android


https://code.google.com/p/mjpeg-stream-client/source/browse/trunk/client.py

http://wiki.ubuntuusers.de/MJPG-Streamer
https://github.com/jacksonliam/mjpg-streamer



Ermitteln der Höhe über Gund
Baromatrische Höhen messer können nur Messen wie hoch sie über 0m sind. D.h. wir müssen die Höhe für aktuelle GPS Position finden. Google API hilft hierbei

http://maps.googleapis.com/maps/api/elevation/json?locations=50.823816,6.895600&sensor=true

{
   "results" : [
      {
         "elevation" : 70.85005187988281,
         "location" : {
            "lat" : 50.823816,
            "lng" : 6.8956
         },
         "resolution" : 152.7032318115234
      }
   ],
   "status" : "OK"
}



elevation kann dazu von der Barometrischen Höhe abgezogen werden und wir haben die Höhe über Grund.

https://developers.google.com/maps/documentation/elevation/#ElevationRequests



Motorsteuerung

Ziel am ende einen wert von 0 - 100 zur Steuerung der ESC


Main Props

roll / pitch = sensor + steuerung
yaw = steuerung - kompass

B4=pitch
B5=roll
B6=yaw
B7=alt

VL=(1+(B4+B5+B6)/3)+B7
VR=(1+(B4+(B5*-1)+(B6*-1))/3)+B7
HR=(1+((B4*-1)+B5+(B6*-1))/3)+B7
HL=(1+((B4*-1)+(B5*-1)+B6)/3)+B7








This project is a privat project and you can use the code for your own purpose. I am not reliable for damage made with this code. So if you destroy your own equipment, it's your business
