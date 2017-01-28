# jodel_fetcher.py

import schedule
import time

def fetch(long=0, lat=0, city=""):
	print "Fetching Jodels from", city, "at (", lat, long, ")"
	# TODO: Implement fetching...

schedule.every(5).seconds.do(fetch)

while True:
	schedule.run_pending()
