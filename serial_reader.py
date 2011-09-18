#!/usr/bin/env python
# encoding: utf-8
"""
serial.py
Created by Michael Dory | doryexmachina on 2011-09-18.
"""

import serial
import os

# define the arduino's location and listening speed
arduinoPort = '/dev/tty.usbmodemfd131'
arduinoSpeed = '9600'

# start it all up 
# (with aruments here for when I get off my butt and add command line parsing)
def main(arduinoPort,arduinoSpeed,arguments=None):
	
	#	open up the serial port
	ser = serial.Serial(arduinoPort, arduinoSpeed)
	
	#
	while 1:
		val = ser.readline()
		print val
		print(repr(val)[1:-1])
		if (val == '.\r\n'):
			#print val
			print 'Preparing to deploy!'
			os.system('git commit -am "this was deployed by an Arduino!"')
			os.system('git push heroku master')
			print 'Preparing to deploy!'
			exit()
			

# do that thang!
if __name__ == "__main__":
	print '\nFiring up...\n'
	main(arduinoPort,arduinoSpeed)
