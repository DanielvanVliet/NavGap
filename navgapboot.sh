#! /bin/sh
### INFO
# Boots up NavGap.sh in /home/pNavGap/
### END INFO

USER=root
HOME=/root
export USER HOME
case "$1" in
	start) ### only this is currently played
		echo "### Updating List ###"
		sudo iwlist wlan0 scan |grep ESSID > ~/github/NavGap/log.csv
		;;
	stop) ## update?
		echo "### Stop Bootup ###"
		echo "Stop Bootup" > /home/pi/navgap/log.csv
		;;
	update) ## updates list
		sudo iwlist wlan0 scan |grep ESSID > /home/pi/navgap/log.csv
		;;
	*)
		echo "### Usage: /ect/init.d/NavGapBoot {start|stop} ###"
		exit 1
		;;
	esac
	exit 0
