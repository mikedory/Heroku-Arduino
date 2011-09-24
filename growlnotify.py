#!/usr/bin/env python
"""
Must have py-Growl installed:
	sudo pip install py-Growl
"""

import sys
import os
from Growl import GrowlNotifier
from Growl import Image

def notify(header,body):
	gi = Image.imageFromPath('static/images/arduino_logo.png')
	gn = GrowlNotifier(applicationName="Notify!",notifications=['alert','notification'],applicationIcon=gi)
	gn.register()
	gn.notify(noteType='notification',title=header,description=body,icon=gi)

