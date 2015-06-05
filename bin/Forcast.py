import os
import sys
import time
import datetime
from pydap.client import open_url
from gps import *
import math
import numpy as np

#script to get and log forcast data

def get_forecast(fix):
	# TODO allowing different variables as options

	url = "http://nomads.ncep.noaa.gov:9090/dods/gfs_1p00/gfs" + build_url()
	
	dataset = open_url(url)
	gust = dataset.gustsfc
	
	lat = get_lat(fix.latitude)
	lon = get_lon(fix.longitude)

	grid = gust.array[0:10,lat-10:lat+10,lon-10:lon+10]
	
	np.save("logs/forecasts/" + build_url(), grid)	
	grid = None

	print "Download Complete. Numpy File Saved:"
	print build_url()

def get_lat(lat):
	return int(math.floor(lat))

def get_lon(lon):
	if lon >= 0:
		return lon
	else:
		return int(abs(lon)) + 180

def build_url():
	curr_time = datetime.datetime.now()
	hour = curr_time.hour
	if not os.path.exists("logs/forecasts/" + curr_time.strftime("%Y%m%d")):
		os.mkdir("logs/forecasts/" + curr_time.strftime("%Y%m%d"))

	if hour < 6:
		day = curr_time - datetime.timedelta(1)
		return day.strftime("%Y%m%d") + "/gfs_1p00_18z"
	elif hour >= 6 and hour < 12:
		return curr_time.strftime("%Y%m%d") + "/gfs_1p00_00z"
	elif hour >= 12 and hour < 18:
		return curr_time.strftime("%Y%m%d") + "/gfs_1p00_06z"
	elif hour >= 16 and hour < 24:
		return curr_time.strftime("%Y%m%d") + "/gfs_1p00_12z"


#block for testing
"""
if __name__ == '__main__':
	session = gps(mode=WATCH_ENABLE)
	active = True

	while active:
		try:
			report = session.next()
			if report['class'] == 'TPV':
				get_forecast(session.fix)
				active = False
	
				print "DONE"
	
		except KeyError:
			pass
		except KeyboardInterrupt:
			quit()
		except StopIteration:
			session = None
			print "terminated"
"""
