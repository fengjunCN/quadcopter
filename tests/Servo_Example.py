#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

#servoMax = 3688  # Min pulse length out of 4096
servoMin = 200  # Min pulse length out of 4096
#servoMin = 3892  # Max pulse length out of 4096
servoMax = 650  # Max pulse length out of 4096

#def setServoPulse(channel, pulse):
#  pulseLength = 1000000                   # 1,000,000 us per second
#  pulseLength /= 60                       # 60 Hz
#  print "%d us per period" % pulseLength
#  pulseLength /= 4096                     # 12 bits of resolution
#  print "%d us per bit" % pulseLength
#  pulse *= 1000
#  pulse /= pulseLength
#  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(50)                        # Set frequency to 60 Hz
while (True):
  Eingabe = input("% of throttle: ")
  if Eingabe > 100:
    print "Invalid Input"
    next
  Eingabe = Eingabe / 100.0 * 450
  Eingabe = Eingabe + servoMin
  print "Set Value: " + str(Eingabe)
  pwm.setPWM(0, 0, int(Eingabe))



