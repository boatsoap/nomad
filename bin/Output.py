import serial
import json
from pprint import pprint

class Output:

	def __init__(self):
		#instantiate serial connection
		#self.ser = serial.Serial('/dev/ttyACM0', 9600)

		#load previous values to ensure servo spins the correct direction
		with open('bin/output.json') as data_file:
			self.data = json.load(data_file)

		pprint(self.data)
	
	def set_servo(self, n):
		self.ser.write(new_course)
	
	def close_serial(self):
		#end serial connection and sleep arduino
		print "close"

#block for testing
if __name__ == '__main__':
	output = Output()

