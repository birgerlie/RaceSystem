#!/usr/bin/env python

from handlers.base import BaseHandler

class RaceHandler(BaseHandler):
    def get(self):
        self.redirect("/map.html")


