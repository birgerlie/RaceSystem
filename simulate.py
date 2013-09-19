#!/usr/bin/env python

from math import *
import httplib, urllib
from random import randint
import time
from geopy import distance  
from geopy.point import Point
from settings import settings
from pymongo import MongoClient

class LatLon():
	def __init__(self, lat,lng):
		self.lat = lat
		self.lng = lng

	def distance(self,other):
		return distance.distance(Point(self.lat,self.lng),Point(other.lat,other.lng)).meters * 0.8684

	def bearing(self, other ):
		lat2,lon2 = other.lat,other.lng
		dLon = lon2 - self.lng
		y = sin(dLon) * cos(lat2)
		x = cos(self.lat) * sin(lat2) \
		    - sin(self.lat) * cos(lat2) * cos(dLon)
		d =  degrees(atan2(y, x))
		
		if d < 0.0 :
			return 360.0 + d
		else:
			return d

	def __dict__(self):
		return {"lat": self.lat, "lng":self.lng }



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
	
	min_dist = 0.005
	current_mark = boats_marks[last_pos[bid]]




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


marks = []
boats_marks= {}
if __name__ == "__main__":
	
 	db =  MongoClient().race_data
 	race = db.race.find_one()
 	
 	for k,v in race['marks'].iteritems():
 		marks.append( LatLon(v['pos']['lat'],v['pos']['lng']))

 	race_id = str(race['_id'])
 	print "Race: %s " % race['title']

	headers={"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	update_freq = 1000  #simulated update freq



	boats = [
			{
	       'lat':59.4,
	       'lng':10.2,
	       'hdg':150.0,
	       'speed':10.5,
	       'utc' : time.time(),
           'id' : 'Rett Fram',
           'nr' : 'NOR 123',
           'skipper' : 'Kristoffer Brunner Lie',
           'race' :race_id
	       },
	       {
	       'lat':59.41,
	       'lng':10.25,
	       'hdg':150.0,
	       'speed':10.5,
	       'utc' : time.time(),
           'id' : 'Zikk Zakk',
           'nr' : 'NOR 29110',
           'skipper' : 'Per Kristoffer Lie',
           'race' :race_id
	       },
	       {
	       'lat':59.445045,
	       'lng':10.250284,
	       'hdg':150.0,
	       'speed':10.5,
	       'utc' : time.time(),
           'id' : 'Glefs',
           'nr' : 'NOR 26548',
			'skipper' : 'Birger Kristoffer Lie',
			'race' :race_id
	       },
	        {
	       'lat':59.46,
	       'lng':10.26,
	       'hdg':150.0,
	       'speed':10.5,
	       'utc' : time.time(),
           'id' : str('Team NZ'),
           'nr' : 'NZL 32',
			'skipper' : 'Dean Barker',
			'race' :race_id
	       }
	]

	server = "%s:%s" % (settings['server'],settings['port'])

	conn = httplib.HTTPConnection(server)
	print 'server:' , server
	count = 0
	bid = 'id'

	for boat in boats:
		boats_marks[boat[bid]] = marks[0]

	while(True):

		conn = httplib.HTTPConnection(server)
		i = count % len(boats)
		boats[i] = create_data(boats[i])

		print boats[i]	

		params = urllib.urlencode(boats[i])
		conn.request("POST", "/pos", params, headers)
		time.sleep(1)
		count +=1
	





	




