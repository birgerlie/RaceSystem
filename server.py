#!/usr/bin/env python

import logging
import unicodedata


import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket

from tornado.options import define, options
from pymongo import MongoClient, GEO2D

from settings import settings
from urls import url_patterns


        
tornado.options.parse_command_line()

class Application(tornado.web.Application):
    
    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)
        self.db = MongoClient().race_data
        self.db.race.create_index([("loc", GEO2D)])
        self.sock = []

    
        
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()            




if __name__ == "__main__":
    main()





