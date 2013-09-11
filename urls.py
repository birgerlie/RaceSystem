#!/usr/bin/env python
from handlers.race import RaceHandler
from handlers.race_create import RaceCreateHandler
from handlers.home import HomeHandler
from handlers.report_position import ReportPositionHandler
from handlers.web_socket_broadcaster import WebSocketBroadcasterHandler
#from handlers.race_list import RaceListHandler


url_patterns =[
                        (r'/', HomeHandler),
                        (r'/create', RaceCreateHandler),
                        (r"/race/(.+)", RaceHandler),
                        (r"/sock", WebSocketBroadcasterHandler),   
                        (r"/pos", ReportPositionHandler),
 #                       (r"/list", RaceListHandler)
                ]