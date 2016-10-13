from bluepy.btle import Scanner, DefaultDelegate
import time
import logging
import globals

class Nut():
	def __init__(self):
		self.name = 'nut'

	def isvalid(self,name,manuf=''):
		if name.lower() == self.name:
			return True
			
	def parse(self,data):
		action={}
		action['present'] = 1
		return action

globals.COMPATIBILITY.append(Nut)