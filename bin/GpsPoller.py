import os
import sys
from gps import *
import threading

class GpsPoller(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)
		self.session = gps(mode=WATCH_ENABLE)
		self.current_value = None
		self.running = True 

	def get_current_value(self):
		return self.session

	def run(self):
		while self.running:
			self.session.next()


