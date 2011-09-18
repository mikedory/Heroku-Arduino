#!/usr/bin/env python
# encoding: utf-8
"""
serial_reader.py
Created by Michael Dory | doryexmachina on 2011-09-18.
"""

import serial
import os
import time

# define the arduino's location and listening speed
arduinoPort = '/dev/tty.usbmodemfd131'
arduinoSpeed = '9600'

# start it all up 
# (with aruments here for when I get off my butt and add command line parsing)
def main(arduinoPort,arduinoSpeed,arguments=None):
	
	#	open up the serial port
	ser = serial.Serial(arduinoPort, arduinoSpeed)
	
	# watch out for the right characters
	while 1:
		val = ser.readline()
		#print(repr(val)[1:-1]) # print out the invisible characters (handy for debugging)

		# if we get a 'd' from the arduino, a button was pressed
		if (val == 'd\r\n'):
			
			# deploy!
			print 'Preparing to deploy!'
			os.system('git commit -am "this was deployed by an Arduino!"')
			os.system('git push heroku master')

			# wait a bit...
			time.sleep(5) # hang out for five seconds
			

# do that thang!
if __name__ == "__main__":
	print '\nFiring up...\n'
	main(arduinoPort,arduinoSpeed)
