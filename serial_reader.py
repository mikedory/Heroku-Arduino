#!/usr/bin/env python
# encoding: utf-8
"""
serial.py
Created by Michael Dory | doryexmachina on 2011-09-18.
"""

import serial
import sys
import os

arduinoPort = '/dev/tty.usbmodemfd131'
arduinoSpeed = '9600'
ser = serial.Serial('/dev/tty.usbmodemfd131', '9600')

# this is where the magic happens
def main(arduinoPort,arduinoSpeed,arguments=None):
		
	ser = serial.Serial(arduinoPort, arduinoSpeed)
	
	while 1:
		val = ser.readline()
		if (val == 'deploy!'):
			#print val
			print 'heeere we go!'

# do that thang!
if __name__ == "__main__":
	print '\nFiring up...\n'
	main(arduinoPort,arduinoSpeed)
