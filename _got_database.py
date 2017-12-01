#!/usr/bin/env python2.7

import csv

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

  def _load_houses(self):
    houses = {k: [] for k in self.get_houses()}
    for k, v in self.characters.items():
      house = self.get_house(k)
      if house != -1:
        houses[house].append(k)
    return houses

  def _load_dead(self):
    dead = lambda x: not self.is_alive(x)
    return list(filter(dead, self.get_characters()))

  def _load_books(self):
    return {k: {
      'num_deaths': len(self.get_book_deaths(k)),
      'num_intros': len(self.get_book_intros(k)),
      'dead': self.get_book_deaths(k),
      'intros': self.get_book_intros(k) 
      } for k in range(1, 6)}

  def get_books(self):
    return self.books

  def get_book(self, book):
    return self.books[book]

  def get_characters(self):
    return self.characters.keys()

  def get_houses(self):
    key = 'allegiances'
    house = lambda x: x[key] if key in x and x[key] != 'None' else ''
    return set(house(v) for k, v in self.characters.items()) - set('')

  def get_field(self, character, field):
    try:
      return self.characters[character][field]
    except:
      return -1

  def is_alive(self, character):
    return self.get_field(character, 'is_alive')


  def get_gender(self, character):
    try:
      return 'Male' if self.characters[character]['gender'] else 'Female'
    except:
      return -1


  def get_nobility(self, character):
    try:
      return 'Noble' if self.characters[character]['nobility'] else 'Commoner'
    except:
      return -1

  def get_house(self, char):
    house = self.get_field(char, 'allegiances')
    return house if house != 'None' else -1

  def get_birth_year(self, char):
    return self.get_field(char, 'date_of_birth')

  def get_death_year(self, char):
    return self.get_field(char, 'death_year')

  def get_death_book(self, char):
    return self.get_field(char, 'book_of_death')

  def get_intro_book(self, char):
    book = [self.get_field(char, 'book{}'.format(i+1)) for i in range(5)]
    return book.index(1) + 1 if 1 in book else 0

  def get_death_chapter(self, char):
    return self.get_field(char, 'death_chapter')

  def get_intro_chapter(self, char):
    return self.get_field(char, 'book_intro_chapter')

  def get_title(self, char):
    return self.get_field(char, 'title')

  def get_book_deaths(self, book):
    key = 'book_of_death'

    match = lambda x: key in self.characters[x] and self.characters[x][key] == book
    return list(filter(match, self.dead))

  def get_book_intros(self, book):
    return list(filter(lambda x: self.get_intro_book(x) == book, self.get_characters()))
