#!/usr/bin/env python2.7

import cherrypy, json

class house_controller(object):
  
  def __init__(self, database):
    self.database = databse

  def GET(self, house_name=None):
    output = { "result" : "success" }

    if not house_name:
      output["names"] = self.database.get_houses()
    else:
      if house_name in self.database.houses:
        output = self.database.houses[house_name]
        output["result"] = "success"

    if not output:
      output = { "result" : "error" }

    return json.dumps(output)
