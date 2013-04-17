import tornado.ioloop
import tornado.web
import os
import json
import logging

import tornado.ioloop
import tornado.web
import tornado.websocket

from tornado.options import define, options

define("port", default=5000, help="run on the given port", type=int)


WEBSOCKS = []
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("/static/map.html")

class PositionHandler(tornado.web.RequestHandler):
    def get(self):
        lat =  self.get_argument("lat")
        lon = self.get_argument("lon")
        print lat,lon
	
    def post(self):
        global WEBSOCKS
        
        lat =  self.get_argument("lat")
        lng = self.get_argument("lng")
        
        latlng ={
        'lat':lat,
        'lng':lng,
        'device': 'foo'
        }
        data = json.dumps(latlng)
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
        
settings = {
  'static_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), ""),
}

tornado.options.parse_command_line()
application = tornado.web.Application([
                            (r"/", MainHandler),
                            (r"/sock", WebSocketBroadcaster),	
                            (r"/pos", PositionHandler)           
                            ],
                            **settings)


if __name__ == "__main__":
    application.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()






