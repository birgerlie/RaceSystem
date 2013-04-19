#!/usr/bin/env python
from handlers.base import BaseHandler
import json

class ReportPositionHandler(BaseHandler):
    def post(self):
        global WEBSOCKS
        
        lat =  self.get_argument("lat")
        lng = self.get_argument("lng")
        gps_info = {
	       'lat':self.get_argument("lat"),
	       'lng':self.get_argument("lng"),
	       'hdg':self.get_argument("hdg"),
	       'speed':self.get_argument("speed"),
	       'utc' : self.get_argument("time") 
	       }
	
        data = json.dumps(gps_info)
        print data
        for sock in WEBSOCKS:
            sock.write_message(data)