#!/usr/bin/env python

from handlers.base import BaseHandler


class HomeHandler(BaseHandler):
    def get(self):
		self.set_header('Access-Control-Allow-Origin', '*')
		self.set_header('Access-Control-Allow-Methods', 'POST, OPTIONS, GET')
		self.set_header('Access-Control-Max-Age', 1000)
		self.set_header('Access-Control-Allow-Headers', '*')
		self.set_status(200)
        

		render_type = self.get_argument('format', 'html')
		items=self.db.race.find()
        
		if items == None:
			items = []

		if render_type == 'html':
			self.render('home.html', title='Show races', events=items)
		else:
			data = {}
			for item in items:
				_id = '%s' % item['_id']
				item['_id'] = _id 
				data[_id]= item

			self.write(data)

