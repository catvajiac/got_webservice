#!/usr/bin/env python2.7

import cherrypy, json

class dead_controller(object):
  
  def __init__(self, database):
    self.database = databse

  def GET(self, house_name=None, book=None):
    output = { "result" : "success" }

    if house_name:
      if house_name in self.database.houses:
        #TODO: get dead people by house
        output = self.database.dead
        output["result"] = "success"
    elif book:
      if book in self.database.books:
        output = self.database.books[book][dead]
        output["result"] = "success"
    else:
      output["names"] = self.database.get_dead()

    if not output:
      output = { "result" : "error" }

    return json.dumps(output)
