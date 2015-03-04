#!/usr/bin/python

import sys, getopt
import thread
import time
import logging
sys.path.append('.')
import RTIMU
import os.path
import math
from Adafruit_PWM_Servo_Driver import PWM

def ReadSensor(status):
	SETTINGS_FILE = "RTIMULib"
	
	#print("Using settings file " + SETTINGS_FILE + ".ini")
	#if not os.path.exists(SETTINGS_FILE + ".ini"):
	  #print("Settings file does not exist, will be created")
	
	s = RTIMU.Settings(SETTINGS_FILE)
	imu = RTIMU.RTIMU(s)
	
	#print("IMU Name: " + imu.IMUName())
	
	if (not imu.IMUInit()):
	    #print("IMU Init Failed");
	    sys.exit(1)
	#else:
	    #print("IMU Init Succeeded");
	
	poll_interval = imu.IMUGetPollInterval()
	#print("Recommended Poll Interval: %dmS\n" % poll_interval)
	logging.debug('ReadSensor, Thread started')
	while 1:
		if imu.IMURead():
			# x, y, z = imu.getFusionData()
			tmpgyrox = math.degrees(imu.getIMUData()["fusionPose"][0])
			if tmpgyrox < 0:
				tmpgyrox *= -1
			status["gyro-x"] = tmpgyrox
		
		time.sleep(0.001)
		logging.debug('ReadSensor, Loop')
		#GPS
		#altitude by barometric sensor
		#read altitude by google api
		#roll & pitch
		#yaw compass
		# read distance sensor
		# set ready preflight check 1
		# read sonsors for ~30sec if no change set ready for flight 1
		# update sonsors roll & pitch every 1ms
		# update gps barometric sensor, yaw, distane sensor 100ms
		# update altitude over ground every 1sec
		# if something missing, set emergency state (hold position as possible)


def PrintData(status):
	logging.debug('ReadSensor, Thread PrintData')
	while 1:
		time.sleep(1)
		logging.debug('PrintData, Loop')

def ControlProps(status):
	logging.debug('ReadSensor, Thread ControlProps')
	pwm = PWM(0x40)
	servoMin = 230  # Min pulse length out of 4096
	servoMax = 650  # Max pulse length out of 4096
	pwm.setPWMFreq(50)                        # Set frequency to 60 Hz
	print "Start"
	pwm.setPWM(0, 0, int(200))
	time.sleep(1)
	print "Full throttle"
	pwm.setPWM(0, 0, int(650))
	time.sleep(3)
	print "low throttle"
	pwm.setPWM(0, 0, int(200))
	time.sleep(10)
	print "Starting...."
	start = 10
	try:
		while 1:
			time.sleep(0.002)
			logging.debug('ControlProps, Loop')
			value = status["gyro-x"] / 180.0 * 410
			Eingabe = value + servoMin + start
			print Eingabe
			pwm.setPWM(0, 0, int(Eingabe))
	except KeyboardInterrupt:
		pwm.setPWM(0, 0, ServoMin)
		print "Reset Servo!!"
		raise
	except:
		raise

def ReadInput(status):
	logging.debug('ReadInput, Thread ReadInput')
	while 1:
		time.sleep(1)
		logging.debug('ReadInput, Loop')

def CAM(status):
	logging.debug('CAM, Thread ReadInput')
	while 1:
		time.sleep(1)
		logging.debug('CAM, Loop')

status={}
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='/var/log/copter.log',level=logging.DEBUG)
logging.debug('Main: Started Up')

# check stare of vpn tunnel MUST be online

try:
	thread.start_new_thread( ReadSensor, (status, ) )
	thread.start_new_thread( PrintData, (status, ) )
	thread.start_new_thread( ControlProps, (status, ) )
	thread.start_new_thread( ReadInput, (status, ) )
	thread.start_new_thread( CAM, (status, ) )
except:
	logging.warning('Main: WARNNG a thread gave back some error')

while 1:
   pass
