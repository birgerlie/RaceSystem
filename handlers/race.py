#!/usr/bin/env python

from handlers.base import BaseHandler
#import pymongo
from bson import ObjectId

class RaceHandler(BaseHandler):
    def get(self, raceId):
		print raceId
		_id = ObjectId(raceId)
		race = self.db.race.find_one({'_id' : _id})
		marks = []
 		mark_list = []
		for mark_key in race['marks']:
			mark_pos = race['marks'][mark_key]['pos']
			name = race['marks'][mark_key]['name']

			m = {'m_id': int(mark_key), 'lat': mark_pos['lat'], 'lng':mark_pos['lng']}
			mark_list.append(m)

			marks =  sorted(mark_list, key=lambda mark: mark['m_id'] )


		self.render("race.html",race=race, marks = marks)


