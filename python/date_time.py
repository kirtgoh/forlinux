#!/usr/bin/python

from datetime import date
# from datetime import time
from datetime import datetime 

def main():

	## DATE OBJECTS
	# 1 Get today's date from the simple today() method from the date class
	today = date.today()
	print "Today's date is ", today

	# 2 print out the date's individual components
	print "Date Components: ", today.day, today.month, today.year

	# 3 retrieve today's weekday (0=Mondy, 6=Sunday)
	print "Today's Weekday #: ", today.weekday()

	## DATETIME OBJECTS
	# 4 Get today's date from the datetime class
	now = datetime.now()
	print "The current date and time is ", now 

	# 5 get the current time
	print "The current time is ", now.time()

	# 6 weekday returns 0 (monday) through 6 (sunday) 
	wd = date.weekday(today)

	# Days start at 0 for Monday
	days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
	print "Today is day number %d " % wd
	print "Which is a " + days[wd]

if __name__ == '__main__':
	main()
		

