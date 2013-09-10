#!/usr/bin/env python

from handlers.base import BaseHandler


class HomeHandler(BaseHandler):
    def get(self):

    	render_type = self.get_argument('format', 'html')

        items=self.db.race.find()
        data = {'data' : items}

        if items == None:
        	items = []

        if render_type == 'html':
        	self.render('home.html', title='Show races', events=items)
        else:
        	self.write(data)

