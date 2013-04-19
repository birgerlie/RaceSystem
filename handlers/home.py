#!/usr/bin/env python

from handlers.base import BaseHandler


class HomeHandler(BaseHandler):
    def get(self):
        items=self.db.race.find()
        self.render('home.html', title='Show races', events=items)
