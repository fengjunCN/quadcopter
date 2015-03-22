#Quadcopter Project based on an Raspberry Pi

This is an project where i try to bring up an raspberry controlled quadcopter can be controlled by PC Client, Raspberry remote Client and by server based flight plan


#Thinks done so far


Ordered an 
- raspberry pi B+
- 4x Emax MT2216 V2 Brushless Motor 810kv 3S-4S 11,1V-14,8V
- 4x Emax BLHeli Multicopter Brushless Regler 12A 2S - 4S 7,4V-14,8V Lipo 1A BEC 
- Adafruit 16-Channel 12-bit PWM/Servo Driver - I2C interface - PCA9685
- Adafruit 9-DOF Accel/Mag/Gyro+Temp Breakout Board - LSM9DS0
- TOPFUEL LIPO-AKKU 20C-ECO-X 2400MAH 4S
- LIPO Charger
- Adafruit MPL3115A2 - I2C Barometric Pressure/Altitude/Temperature Sensor (not configured yet)
- Adafruit 3-Achsen Magnetometer Board - HMC5883L (not configured yet)


* Try to run an LED based on the Servo Driver. This was a little bit research since the LED Driver is with 12 bit a little bit tricky to set. Always need to change 2 register valies on i2c bis if you want to have only one change. (Test will be uploaded soon)

Finally this was Succesfull using bash (quite basic since only research and i tried to understand the system)

* Try to run an Servo (the most basic servo there is on the market)
Sucessfull after i understand the Pule length stuff with 50Hz Freq (20ms) and length of 1-2ms. Test Script in python. This is basicly an change of the Adafruit Samples (Thanks for that)


* First steps in makeing motors controlling the balance on only one axis.
* Security switch off. learned the hard way in grep in high speed fan... ouch
* OO in python for the 4 rotors. seems more adequat.
