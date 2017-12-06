#!/usr/bin/env python2.7

import cherrypy, json

class options_controller(object):

  def OPTIONS(self, *args, **kargs):
    return ""