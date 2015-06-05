import os
import sys
import threading
import time
from subprocess import call
from bin.GpsPoller import GpsPoller
import bin.Forcast as forecast
import bin.Output as output
import bin.Logger as logger

class Controller():

	def __init__(self):
		#different states of the program
		self.finding_fix = False
		self.getting_grib = False
		self.setting_course = False

		#classes controlled by controller
		self.gpsp = None
		self.logger = None
		self.forcast = None

		#object variables
		self.curr_fix = None

	def get_threads(self):
		return self.threads
	
	def get_current_step(self):
		if self.finding_fix:
			return "fixing"
		elif self.getting_grib:
			return "gribbing"
		elif self.setting_course:
			return "coursing"
	
	def end(self):
		self.finding_fix = False
		self.getting_grib = False
		self.setting_course = False
		self.gpsp = None
	
	def main(self):
		print "Beginning Main Loop"
		while(True):
			print "Aquiring Accurate Fix"
			call(['./bin/gpsd_toggle.sh'])
			self.curr_fix = self.fix()

			print "Fix: " + str(self.curr_fix.fix.latitude) + ", " + str(self.curr_fix.fix.longitude)
			logger.write_file(self.curr_fix.fix)

			print "Downloading Forecast Information"
			forecast.get_forecast(self.curr_fix.fix)
			

			call(['./bin/gpsd_toggle.sh'])
			print "Sleeping 6 hours"
			time.sleep(21600)

	def fix(self):	
		#control flow for the program
		#find fix first
		try:
			self.finding_fix = True
			self.gpsp = GpsPoller()
			self.gpsp.start()
			while self.finding_fix:
				report = self.gpsp.get_current_value()
				if report.fix.epx < 30 and report.fix.epy < 30:
					self.gpsp.running = False
					self.finding_fix = False
					return self.gpsp.get_current_value()
			sleep(5)
		except: 
			self.gpsp.running = False
			self.finding_fix = False
			self.gpsp = None
			print "unexpected error:", sys.exc_info()[0]


if __name__ == '__main__':
	print "Starting Navigation"
	controller = Controller()
	controller.main()
	#while(True):
	#	print "Aquiring Accurate Fix"
	#	curr_fix = controller.fix()

	#	forecast.get_forecast(curr_fix.fix)

	#	print "Sleeping for 6 hours"
	#	time.sleep(21600)
