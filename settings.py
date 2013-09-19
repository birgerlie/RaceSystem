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

import environment


path = lambda root,*a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

define("port", default=8888, help="run on the given port", type=int)
#define("server", default='localhost', help="set the host", type=str)
define("server", default='http://ec2-50-112-26-56.us-west-2.compute.amazonaws.com', help="set the host", type=str)


settings = dict(
                     static_path=os.path.join(os.path.dirname(__file__), "static"),
                     template_path=os.path.join(os.path.dirname(__file__), "templates"),
                     site_title=u"Compete with your friends",
                     debug=True,
                     server=options.server,
                     port=options.port
                    )                



# if options.config:
#     tornado.options.parse_config_file(options.config)