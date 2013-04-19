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

define("port", default=8080, help="run on the given port", type=int)


settings = dict(
                     static_path=os.path.join(os.path.dirname(__file__), "static"),
                     template_path=os.path.join(os.path.dirname(__file__), "templates"),
                     site_title=u"Compete with your friends",
                     debug=True
                    )                


# if options.config:
#     tornado.options.parse_config_file(options.config)