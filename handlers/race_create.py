#!/usr/bin/env python
from handlers.base import BaseHandler


class RaceCreateHandler(BaseHandler):

    def get(self):
        id = self.get_argument('id', None)
        race = None

        if id:
            
            race=self.db.race.find_one({"id":id})
            print race

        self.render('new_race_event.html', race=race)

    def post(self):

        race_info = {
        'title':self.get_argument("title", None),
        'desc':self.get_argument("desc", None),
        'started':self.get_argument("started", False),
        'start':[self.get_argument("s_lat", None),self.get_argument("s_lng", None)],
        'goal':[self.get_argument("f_lat", None),self.get_argument("f_lng", None)],
        'creator':'birger.lie@gmail.com'
        }   
        self.db.race.insert(race_info)
