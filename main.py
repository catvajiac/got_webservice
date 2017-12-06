#!/usr/bin/env python3

import cherrypy
from _got_database import _got_database
from character_controller import character_controller
from house_controller import house_controller
from dead_controller import dead_controller
from book_controller import book_controller
from options_controller import options_controller 

def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "*"


#######################
## CREATE DISPATCHER ##
#######################

def start_service():
  dispatcher = cherrypy.dispatch.RoutesDispatcher()
  conf = { 'global' : { 'server.socket_host' : 'localhost', 
                        'server.socket_port' :51062,
                        'tools.CORS.on': True
                      },
           '/'      : { 'request.dispatch' : dispatcher }
         }

  database = _got_database()

  ######################
  #CHARACTER CONTROLLER#
  ######################

  char_c = character_controller(database)

  #GET
  dispatcher.connect('char_get', '/characters/', controller=char_c, action='GET',
    conditions=dict(method=['GET']))

  #GET (char_name)
  dispatcher.connect('char_get_char_name', '/characters/:char_name', controller=char_c, 
    action='GET', conditions=dict(method=['GET']))

  ##################
  #HOUSE CONTROLLER#
  ##################

  house_c = house_controller(database)

  #GET
  dispatcher.connect('house_get', '/houses/', controller=house_c, action='GET',
    conditions=dict(method=['GET']))

  #GET (house_name)
  dispatcher.connect('house_get_house_name', '/houses/:house_name', controller=house_c, 
    action='GET', conditions=dict(method=['GET']))

  #################
  #DEAD CONTROLLER#
  #################

  dead_c = dead_controller(database)

  #GET
  dispatcher.connect('dead_get', '/dead/', controller=dead_c, action='GET',
    conditions=dict(method=['GET']))

  #GET (book)
  dispatcher.connect('dead_get_book', '/dead/:book', controller=dead_c, action='GET',
    conditions=dict(method=['GET']))


  #################
  #BOOK CONTROLLER#
  #################

  book_c = book_controller(database)

  #GET 
  dispatcher.connect('book_get', '/bookstats/', controller=book_c, action='GET',
    conditions=dict(method=['GET']))

  #GET (book)
  dispatcher.connect('book_get_book', '/bookstats/:book', controller=book_c, action='GET',
    conditions=dict(method=['GET']))

  ##################
  #START THE SERVER#
  ##################
  
  cherrypy.config.update(conf)
  app = cherrypy.tree.mount(None, config=conf)
  cherrypy.quickstart(app)

###################
## MAIN FUNCTION ##
###################

if __name__ == "__main__":
  cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
  start_service()
