import os
import sys
import time


def write_file(fix):
	log_path = "logs/"
	filename = log_path + "location_log.txt"
	curr = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
	loc = "    " + str(fix.latitude) + ", " + str(fix.longitude) + "\n"
	info = "    heading: " + str(fix.track) + ", speed: " + str(fix.speed) + "\n" 
	
	target = open(filename, 'a')
	target.write("\n")
	target.write(curr + "\n")
	target.write(loc)
	target.write(info)
	target.close()

