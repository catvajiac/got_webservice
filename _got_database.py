#!/usr/bin/env python2.7

class _got_database:
  def __init__(self):
    pass

  def load_files(self, dir='.'):
    #self.battles = self._load_file('battles.csv', 2, dir)
    self.character_info = self._load_file('character-deaths.csv', 0, dir)
    predictions = self._load_file('character-predictions.csv', 5, dir)

    for character in self.character_info:
      if character in predictions:
        self.character_info[character].update(predictions[character])

  def _load_file(self, file, key, dir='.'):
    with open('{}/{}'.format(dir, file), 'r') as f:
      data = [line.strip().split(',') for line in f.readlines()]
      labels = [label.lower().replace(' ', '_') for label in data.pop(0)]

      return {line[key]: {k: v for k, v in zip(labels, line)} for line in data}

  def is_dead(self, character):
    if character not in self.character_info:
      return -1

    return not self.character_info[character]['death_year']

  def get_gender(self, character):
    if character not in self.character_info:
      return -1

    return 'Male' if self.character_info[character]['gender'] else 'Female'

  def get_nobility(self, character):
    if character not in self.character_info:
      return -1

    return 'Noble' if self.character_info[character]['nobility'] else 'Commoner'

  def get_house(self, character):
    if character not in self.character_info:
      return -1

    return self.character_info[character]['allegiances']

  def get_birth_year(self, character):
    if character not in self.character_info:
      return -1

    return self.character_info[character]['dateofbirth']
      

  def get_death_year(self, character):
    if character not in self.character_info:
      return -1

    return self.character_info[character]['death_year']

  def get_death_book(self, character):
    if character not in self.character_info:
      return -1

    return self.character_info[character]['death_chapter']

  def get_intro_chapter(self, character):
    if character not in self.character_info:
      return -1

    return self.character_info[character]['book_intro_chapter']

  def get_title(self, character):
    if character not in self.predictions:
      return -1

    return self.predictions[character]['title']
