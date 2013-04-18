#!/usr/bin/env python

import os
import json
import logging
import unicodedata


import tornado.auth
import tornado.httpserver
# import tornado.options
import tornado.ioloop
import tornado.web
import tornado.websocket

from tornado.options import define, options
from pymongo import MongoClient, GEO2D


define("port", default=8080, help="run on the given port", type=int)


WEBSOCKS = []


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db


class ListHandler(BaseHandler):
    def get(self):
        items = ['item 1', 'item 2', 'item 3']
        self.render('race.html', title='Show races', items=items)




class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("/static/map.html")

class PositionHandler(tornado.web.RequestHandler):
    def post(self):
        global WEBSOCKS
        
        lat =  self.get_argument("lat")
        lng = self.get_argument("lng")
        gps_info = {
	'lat':self.get_argument("lat"),
	'lng':self.get_argument("lng"),
	'hdg':self.get_argument("hdg"),
	'speed':self.get_argument("speed"),
	'utc' : self.get_argument("time") 
	}
	
        data = json.dumps(gps_info)
        print data
        for sock in WEBSOCKS:
            sock.write_message(data)
        



class WebSocketBroadcaster(tornado.websocket.WebSocketHandler):
    def open(self):
        print "open socket %r" % self
        global WEBSOCKS
        WEBSOCKS.append(self)

    def on_message(self, message):
        print "got message from socket" % message
        
    def on_close(self):
        print "closed socket %r " % self    
        global WEBSOCKS
        WEBSOCKS.remove(self)
        
tornado.options.parse_command_line()

class Application(tornado.web.Application):
    def __init__(self):
        handlers=[
                        (r'/', ListHandler),
                        (r"/race", MainHandler),
                        (r"/sock", WebSocketBroadcaster),   
                        (r"/pos", PositionHandler),
                ]

        settings=dict(
                     static_path=os.path.join(os.path.dirname(__file__), "static"),
                     template_path=os.path.join(os.path.dirname(__file__), "templates"),
                     debug=True
                    )                

        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = MongoClient().race_data
        self.db.places.create_index([("loc", GEO2D)])




def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()            


if __name__ == "__main__":
    main()





