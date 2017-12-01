#!/usr/bin/env python3

import cherrypy, json

class character_controller(object):
  
  def __init__(self, database):
    self.database = database

  def GET(self, char_name=None):
    output = { "result" : "success" }

    if not char_name:
      output["names"] = self.database.get_characters()
    else:
      char_name = char_name.replace('_', ' ')
      if char_name in self.database.characters:
        output = self.database.get_character(char_name)
        output["result"] = "success"

    if not output:
      output = { "result" : "error" }

    return json.dumps(output)
