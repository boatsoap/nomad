#!/bin/bash
#toggle GPSD service as needed by Controller

case "$(pidof gpsd | wc -w)" in
	0) echo "GPSD not running. Starting Service."
		sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock
		while ! pidof gpsd >> /dev/null ;
		do
			sleep 1
		done
		;;
	1) echo "Killing GPSD process(s)."
		sudo killall gpsd
		;;
esac
