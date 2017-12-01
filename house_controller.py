#!/usr/bin/env python2.7

import cherrypy, json

class house_controller(object):
  
  def __init__(self, database):
    self.database = database

  def GET(self, house_name=None):
    output = { "result" : "success" }

    if not house_name:
      output["houses"] = self.database.get_houses()
    else:
      if house_name in self.database.houses:
        output["names"] = self.database.houses[house_name]

    if not output:
      output = { "result" : "error" }

    return json.dumps(output)
