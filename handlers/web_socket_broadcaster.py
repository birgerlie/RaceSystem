#!/usr/bin/env python

import tornado.websocket
from handlers.base import BaseHandler

class WebSocketBroadcasterHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        print "open socket %r" % self
        self.application.sock.append(self)
        print "connecton count %s" % len(self.application.sock)

    def on_message(self, message):
        print "got message from socket" % message
        
    def on_close(self):
        
        print "closed socket %r " % self    
        self.application.sock.remove(self) 
        print "connecton count %s" % len(self.application.sock)

    @property
    def db(self):
        return self.application.db
