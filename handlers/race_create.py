#!/usr/bin/env python
from handlers.base import BaseHandler
import json
from bson.objectid import ObjectId

class RaceCreateHandler(BaseHandler):

    def get(self):
        id = self.get_argument('id', None)
        race = None 
        marks = None

        if id:
            mark_list = []
            race=self.db.race.find_one({"_id": ObjectId(id)})

            for mark_key in race['marks']:
                mark_pos = race['marks'][mark_key]['pos']

                m = { 'm_id': int(mark_key), 'lat': mark_pos['lat'], 'lng':mark_pos['lng']}
                mark_list.append(m)

            marks =  sorted(mark_list, key=lambda mark: mark['m_id'] )

        self.render('new_race_event.html', race=race, marks=marks)

    def post(self):

        id = self.get_argument('id', None)
        marks = str(self.get_argument("wp", None))
        
        if marks:
            marks = json.loads(marks)
            data = {}
            for mark in marks:
                lat = mark['latLng'][mark['latLng'].keys()[0]]
                lng = mark['latLng'][mark['latLng'].keys()[1]]
                data[ str(mark['index'])]={ 'index':mark['index'],'bearing':mark['bearing'],'distance':mark['distance'],'name': mark['name'], 'pos':{'lat': lat, 'lng': lng }}

            race_info = {
            'title':self.get_argument("title", None),
            'desc':self.get_argument("desc", None),
            'started':self.get_argument("started", False),
            'start': data['0'],
            'goal':data[str(len(data) -1)] ,
            'creator':'birger.lie@gmail.com',
            'marks' : data,
            }   

            if id:
                print 'update race: %s' % race_info['title']  
                # race_info['_id'] = ObjectId(id)
                self.db.race.update({'_id': ObjectId(id)}, race_info)
            else:
                print 'create race: %s' % race_info['title']  
                self.db.race.insert(race_info)
            
            self.redirect('/')
