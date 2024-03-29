#!/usr/bin/env python
from handlers.base import BaseHandler
import json
import calendar
import datetime




class ReportPositionHandler(BaseHandler):
    def post(self):
        # print(self.request  )
        
        skipper = 'Ukjent'
        try:
            skipper = self.get_argument('skipper',None)

        except:
            print ('feil under parsing')

        gps_info = {
	       'lat':self.get_argument("lat", None),
	       'lng':self.get_argument("lng",None),
	       'hdg':self.get_argument("hdg",None),
	       'speed':self.get_argument("speed",None),
	       'utc' : calendar.timegm(datetime.datetime.now().utctimetuple()) ,
           'yacht' : self.get_argument('id',None),
           'nr' : self.get_argument('nr',None),
           'skipper' : skipper,
           'race': self.get_argument('race','None')
	       }


        
        id = gps_info['yacht'] + gps_info['nr']
        id= id.replace(' ', '')
        gps_info['id'] = id


        print gps_info
        if(self.validate_data(gps_info)):       
            data = json.dumps(gps_info)
            # _id = "%s_%s" % (gps_info['id'], gps_info['utc'])
            # gps_info['_id'] =  _id
            
            self.db.pos.insert(gps_info)
            for sock in self.application.sock:
                sock.write_message(data)
        else:   
            print 'error validating data %s' % gps_info

    def validate_data(self, data):
        retval = True
        for d in data:
            if data[d] == None:
                return False

        return True        

