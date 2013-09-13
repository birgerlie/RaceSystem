#!/usr/bin/env python
from handlers.base import BaseHandler
import json

class RaceCreateHandler(BaseHandler):

    def get(self):
        id = self.get_argument('id', None)
        race = None

        if id:
            
            race=self.db.race.find_one({"id":id})
            print race

        self.render('new_race_event.html', race=race)

    def post(self):

        # print self.request

        marks = str(self.get_argument("wp", None))
        

        if marks:
            marks = json.loads(marks)
            data = {}
            for mark in marks:
                data[ str(mark['index'])]={ 'index':mark['index'],'bearing':mark['bearing'],'distance':mark['distance'],  'pos':{'lat': mark['latLng']['nb'], 'lng': mark['latLng']['mb']} , 'name': mark['name']}


            print marks
            race_info = {
            'title':self.get_argument("title", None),
            'desc':self.get_argument("desc", None),
            'started':self.get_argument("started", False),
            'start': data['0'],
            'goal':data[str(len(data) -1)] ,
            'creator':'birger.lie@gmail.com',
            'marks' : data,
            }   


            self.db.race.insert(race_info)
