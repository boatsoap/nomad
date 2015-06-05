from pydap.client import open_url
from sys import argv
from time import gmtime, strftime

#dataset = open_url('http://nomads.ncdc.noaa.gov/thredds/dodsC/gfs-004/201505/20150520/gfs_4_20150520_0000_231.grb2')
dataset = open_url('http://nomads.ncep.noaa.gov:9090/dods/gfs_1p00/gfs20150604/gfs_1p00_00z')
wsg = dataset.gustsfc
#wsg = dataset.Wind_speed_gust

grid = wsg[0:1,90:95,0:10]

#filename = "logs/thredds/" + strftime("%Y%m%d_%H_%M_%S", gmtime()) + ".txt"
#target = open(filename, 'w')

#target.write(str(grid))
#target.close()

print grid
