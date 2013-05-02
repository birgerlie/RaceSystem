#!/usr/bin/env python

from math import *
import httplib, urllib
from random import randint
import time
from geopy import distance  
from geopy.point import Point

boats = 3         #number of competitors
update_freq = 1000  #simulated update freq

def bearing(lat1, lon1, lat2, lon2):
	dLon = lon2 - lon1
	y = sin(dLon) * cos(lat2)
	x = cos(lat1) * sin(lat2) \
	    - sin(lat1) * cos(lat2) * cos(dLon)
	d =  degrees(atan2(y, x))
	
	if d < 0.0 :
		return 360.0 + d
	else:
		return d

gps_info = {
	       'lat':59.445075,
	       'lng':10.250244,
	       'hdg':150.0,
	       'speed':0,
	       'utc' :time.time(),
           'id' :'foo'
	       }


def knot_to_ms(speed):
	return speed/0.514444	
def ms_to_knot(speed):
	return speed*0.514444	

def changing_cource():
	return randint(1,100) % 100 > 50 # .5 chance of changing dir

def create_data(last_pos):
	
	nom = 100000.0

	lng = randint(1,100) / nom
	lat = randint(1,100) / nom

	lat1 = last_pos['lat']
	lng1 = last_pos['lng']
	utc = last_pos['utc']

	last_pos['lat']+=lat
	last_pos['lng']+=lng
	

	lat2 = last_pos['lat']
	lng2 = last_pos['lng']

	last_pos['hdg'] = bearing(lat1,lng1, lat2,lng2)
	last_pos['utc'] = time.time()

	td = time.time() - utc


	d = distance.distance(Point(lat1,lng1),Point(lat2, lng2)).meters
	print "distance: %d" % d 
	print "sec: %d" % td
	ms = d/td
	print 'm/s: %d' %  ms
	knots  = (d/td) * 1.94384

	last_pos['speed'] = knots

	return last_pos


if __name__ == "__main__":
	


	headers={"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	update_freq = 1000  #simulated update freq



	boats = [
			{
	       'lat':59.4,
	       'lng':10.2,
	       'hdg':150.0,
	       'speed':10.5,
	       'utc' : time.time(),
           'id' : 'rett_fram'
	       },
	       {
	       'lat':59.41,
	       'lng':10.25,
	       'hdg':150.0,
	       'speed':10.5,
	       'utc' : time.time(),
           'id' : 'zikk_zakk'
	       },
	       {
	       'lat':59.445045,
	       'lng':10.250284,
	       'hdg':150.0,
	       'speed':10.5,
	       'utc' : time.time(),
           'id' : 'glefs'
	       }
	]

	server = "localhost:8080"
	#server = "ec2-50-16-132-89.compute-1.amazonaws.com:8080"
	conn = httplib.HTTPConnection(server)
	print 'server:' , server
	count = 0
	while(True):

		conn = httplib.HTTPConnection(server)
		i = count % len(boats)
		boats[i] = create_data(boats[i])

		print boats[i]	

		params = urllib.urlencode(boats[i])
		conn.request("POST", "/pos", params, headers)
		time.sleep(1)
		count +=1


    
			
	#resp, content = h.request("http://127.0.0.1:8080/pos", "POST", urlencode(gps_info))
	





	




