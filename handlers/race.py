#!/usr/bin/env python

from handlers.base import BaseHandler
#import pymongo
from bson import ObjectId

class RaceHandler(BaseHandler):
    def get(self, raceId):
    	print raceId
    	_id = ObjectId(raceId)
    	race = self.db.race.find_one({'_id' : _id})
        self.render("race.html",race=race)


