import math


R = 6378.1 #Radius of the Earth

def point_at(lat,lng,distance, heading):
	brng = math.radians(heading)
	d = distance 
	lat1 = math.radians(lat) #Current lat point converted to radians
	lon1 = math.radians(lng) #Current long point converted to radians

	lat2 = math.asin( math.sin(lat1)*math.cos(d/R) +
	     math.cos(lat1)*math.sin(d/R)*math.cos(brng))

	lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),
	             math.cos(d/R)-math.sin(lat1)*math.sin(lat2))

	lat2 = math.degrees(lat2)
	lon2 = math.degrees(lon2)

	return lat2,lon2


def bearing(lat1, lon1, lat2, lon2):
	dLon = lon2 - lon1
	y = sin(dLon) * cos(lat2)
	x = cos(lat1) * sin(lat2) \
	    - sin(lat1) * cos(lat2) * cos(dLon)
	return atan2(y, x)


