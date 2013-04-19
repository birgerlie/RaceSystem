#!/usr/bin/env python
import tornado.web
import tornado.websocket



class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

