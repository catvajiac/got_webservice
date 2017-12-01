#!/usr/bin/env python2.7

import cherrypy, json

class book_controller(object):
  
  def __init__(self, database):
    self.database = database

  def GET(self, book=None):
    output = { "result" : "success" }

    if book:
      if book in self.database.books:
        output = self.database.books[book]
        output["result"] = "success"
    else:
      output = self.database.books

    if not output:
      output = { "result" : "error" }

    return json.dumps(output)
