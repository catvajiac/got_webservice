#!/usr/bin/env python2.7

class _got_database:
  def __init__(self):
    pass

  def load_files(self, dir='.'):
    #self.battles = self._load_file('battles.csv', 2, dir)
    self.deaths = self._load_file('character-deaths.csv', 0, dir)
    self.predictions = self._load_file('character-predictions.csv', 5, dir)

  def _load_file(self, file, key, dir='.'):
    with open('{}/{}'.format(dir, file), 'r') as f:
      data = [line.strip().split(',') for line in f.readlines()]
      labels = [label.lower().replace(' ', '_') for label in data.pop(0)]

      print len(labels), len(data[0])

      return {line[key]: {k: v for k, v in zip(labels, line)} for line in data}

  def is_dead(self, character):
    if character not in self.deaths:
      return -1

    return not self.deaths[character]['death_year']

if __name__ == "__main__":
  db = _got_database()
  db.load_files(dir='data')

  print db.is_dead('Elwood')
  print db.is_dead('Jate Blackberry')
  print db.is_dead('Not a character')
