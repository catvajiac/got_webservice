#!/usr/bin/env python2.7

import csv
import json

class _got_database:
  def __init__(self):
    self._load_files()
    self.houses = self._load_houses()
    self.dead = self._load_dead()
    self.books = self._load_books()

  def _load_files(self, dir='data'):
    self.characters = self._load_file('character-deaths.csv', 'name', dir)
    predictions = self._load_file('character-predictions.csv', 'name', dir)

    # hack to merge things
    for character in self.characters:
      if character in predictions:
        self.characters[character].update(predictions[character])

    for character in predictions:
      if character not in self.characters:
        self.characters[character] = predictions[character]

  def _load_file(self, file, key, dir):
    with open('{}/{}'.format(dir, file), 'r') as f:
      ints = lambda x: int(x) if x.isdigit() else x
      data = [{k: ints(v) for k, v, in line.items()} 
            for line in map(dict, csv.DictReader(f))]
      keys = [d.pop(key) for d in data]

      return {k: v for k, v in zip(keys, data)}

  # TO LOAD HOUSES
  def _load_houses(self):
    houses = {k: [] for k in self.get_houses()}
    for k, v in self.characters.items():
      house = self.get_house(k)
      if house != -1:
        houses[house].append(k)
    return houses

  def get_house(self, char):
    house = self.get_field(char, 'allegiances')
    return house if house != 'None' else -1

  def get_field(self, character, field):
    try:
      return self.characters[character][field]
    except:
      return -1

  # TO LOAD DEATHS
  def _load_dead(self):
    dead = lambda x: not self.is_alive(x)
    return list(filter(dead, self.get_characters()))

  def is_alive(self, character):
    return self.get_field(character, 'is_alive')

  # TO LOAD BOOKS
  def _load_books(self):
    return {k: {
      'num_deaths': len(self.get_book_deaths(k)),
      'num_intros': len(self.get_book_intros(k)),
      'dead': self.get_book_deaths(k),
      'intros': self.get_book_intros(k) 
      } for k in range(1, 6)}

  def get_book_deaths(self, book):
    key = 'book_of_death'
    match = lambda x: key in self.characters[x] and self.characters[x][key] == book
    return list(filter(match, self.dead))

  def get_book_intros(self, book):
    return list(filter(lambda x: self.get_intro_book(x) == book, self.get_characters()))

  def get_intro_book(self, char):
    book = [self.get_field(char, 'book{}'.format(i+1)) for i in range(5)]
    return book.index(1) + 1 if 1 in book else 0

  # FOR BOOK CONTROLLER
  def get_books(self):
    return self.books

  def get_book(self, book):
    return self.books[book]

  # FOR CHARACTER CONTROLLER
  def get_characters(self):
    return list(self.characters.keys())

  def get_character(self, char_name):
    return self.characters[char_name]

  def get_birth_year(self, char_name):
    return self.get_field(char_name, 'date_of_birth')

  def get_death_year(self, char_name):
    return self.get_field(char_name, 'death_year')

  def get_death_book(self, char_name):
    return self.get_field(char_name, 'book_of_death')

  def get_death_chapter(self, char_name):
    return self.get_field(char_name, 'death_chapter')

  def get_gender(self, char_name):
    if char_name in self.characters:
      gender = self.get_field(char_name, 'gender')
      if(gender):
        return 'Male'
      return 'Female'
    else:
      return -1

  def get_intro_chapter(self, char_name):
    return self.get_field(char_name, 'book_intro_chapter')

  def get_nobility(self, char_name):
    if char_name in self.characters:
      is_noble = self.get_field(char_name, 'nobility')
      if(is_noble):
        return 'Noble'
      return 'Commoner'
    else:
      return -1

  def get_title(self, char_name):
    return self.get_field(char_name, 'title')

  # FOR HOUSE CONTROLLER
  def get_houses(self):
    key = 'allegiances'
    house = lambda x: x[key] if key in x and x[key] != 'None' else ''
    houses = set(house(v) for k, v in self.characters.items()) - set('')
    return list(houses)

  # DEAD CONTROLLER
  def get_dead(self):
    return self.dead

  def get_dead_by_book(self, book):
    return self.books[book]['dead']

  def get_dead_by_house(self, house_name):
    names = self.houses[house_name]
    deadlist = []
    for c in names:
      if c in self.dead:
        deadlist.append[c]
    return deadlist
