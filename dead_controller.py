#!/usr/bin/env python2.7

import cherrypy, json

class dead_controller(object):
  
  def __init__(self, database):
    self.database = database

  def GET(self, book=None):
    output = { "result" : "success" }

    if book:
      book = int(book)
      if book in self.database.books:
        output['dead'] = self.database.get_dead_by_book(book)
    else:
      output["dead"] = self.database.get_dead()

    if not output:
      output = { "result" : "error" }

    return json.dumps(output)
