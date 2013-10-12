#!/usr/bin/env python
from handlers.base import BaseHandler
import json
from bson.objectid import ObjectId

class RaceCreateHandler(BaseHandler):

    def get(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, OPTIONS, GET')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        render_type = self.get_argument('format', 'html')
        id = self.get_argument('id', None)
        race = None 
        marks = []

        if id:
            mark_list = []
            race=self.db.race.find_one({"_id": ObjectId(id)})

            if 'marks' in race:
                for mark_key in race['marks']:
                    mark_pos = race['marks'][mark_key]['pos']

                    m = { 'm_id': int(mark_key), 'lat': mark_pos['lat'], 'lng':mark_pos['lng']}
                    mark_list.append(m)

                marks =  sorted(mark_list, key=lambda mark: mark['m_id'] )

        if render_type == 'json':
            self.write( {'marks': marks}) 
                    
        else:
            self.render('new_race_event.html', race=race, marks=marks)

    def post(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, OPTIONS, GET')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        id = self.get_argument('id', None)
        marks = str(self.get_argument("wp", None))
        

        data = {}

        if marks:
            marks = json.loads(marks)

            data = {}
            if 'latLng' not in marks[0]:
                for mark in marks:                
                    mn = 'Mark %s' % mark['m_id']
                    mn = mn.encode('utf-8')
                    data[ str(mark['m_id'])]={ 'index':mark['m_id'], 'name': mn, 'pos':{'lat': mark['lat'], 'lng': mark['lng']}}

            else:
                for mark in marks:
                    lat = mark['latLng'][mark['latLng'].keys()[0]]
                    lng = mark['latLng'][mark['latLng'].keys()[1]]
                    data[ str(mark['index'])]={ 'index':mark['index'],'bearing':mark['bearing'],'distance':mark['distance'],'name': mark['name'].encode('utf-8'), 'pos':{'lat': lat, 'lng': lng }}


        race_info = {
        'started':self.get_argument("started", False),
        # 'start': data['0'],
        # 'goal':data[str(len(data) -1)] ,
        'creator':'birger.lie@gmail.com',
        
        } 
           
        title = self.get_argument("title", '').encode('utf-8')
        desc  = self.get_argument("desc", '').encode('utf-8')
        if title:
            race_info['title'] = title
        
        race_info['desc'] = desc
        if data:
            race_info['marks'] = data

        if id:
            print 'update race: %s' % id 
            self.db.race.update({'_id': ObjectId(id)}, {'$set':race_info})
        else:
            print 'create race: %s' % str(race_info['title'])  
            self.db.race.insert(race_info)
            
            # self.redirect('/')
