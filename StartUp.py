#!/usr/bin/python

import thread
import time
import logging

def ReadSensor(status):
	logging.debug('ReadSensor, Thread started')
	while 1:
		time.sleep(1)
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
	while 1:
		time.sleep(1)
		logging.debug('ControlProps, Loop')
		#control Main Props
		#control sec props
		# each prop roll * pitch * alt * yaw

		# 

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
