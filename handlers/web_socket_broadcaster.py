#!/usr/bin/env python

import tornado.websocket


class WebSocketBroadcasterHandler(tornado.websocket.WebSocketHandler):
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