#!/usr/bin/env python2.7

import cherrypy, json

class book_controller(object):
  
  def __init__(self, database):
    self.database = database

  def GET(self, book=None):
    output = { "result" : "success" }

    if book:
      book = int(book)
      if book in self.database.books:
        output = self.database.get_book(book)
        output["result"] = "success"
    else:
      output = self.database.get_books()

    if not output:
      output = { "result" : "error" }

    return json.dumps(output)
