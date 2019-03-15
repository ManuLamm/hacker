import os
import time
import datetime
import random

fileLocation = r""
for i in range(500):
	year = 2019
	month = random.randint(1,3)
	day =  random.randint(1,14)

	hour =  random.randint(0,23)
	minute =  random.randint(1,60)
	second =  random.randint(0,59)

	date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
	modTime = time.mktime(date.timetuple())


	h = str(bin(random.randint(1,223213123122131231231212))[2:])
	f = open(h,"w+")

	os.utime(h, (modTime, modTime))