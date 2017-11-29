#!/usr/bin/env python2.7

import _got_database
import unittest

class DatabaseUtils(unittest.TestCase):
  db = _got_database._got_database()
  db.load_files(dir="data")

  def test_get_houses(self):
    pass

  def test_is_alive(self):
    self.assertEqual(self.db.is_alive('Arya Stark'), True)
    self.assertEqual(self.db.is_alive('Eddard Stark'), False)
    self.assertEqual(self.db.is_alive('not a character'), -1)

  def test_get_dead(self):
    self.assertTrue('Jon Snow' not in self.db.get_dead())
    self.assertTrue('Arya Stark' not in self.db.get_dead())
    self.assertTrue('Drogo' in self.db.get_dead())

  def test_get_gender(self):
    self.assertEqual(self.db.get_gender('Aegon Targaryen'), 'Male')
    self.assertEqual(self.db.get_gender('Arya Stark'), 'Female')
    self.assertEqual(self.db.get_gender('not a character'), -1)

  def test_get_nobility(self):
    self.assertEqual(self.db.get_nobility('Arya Stark'), 'Noble')
    self.assertEqual(self.db.get_nobility('Will'), 'Commoner')
    self.assertEqual(self.db.get_nobility('not a character'), -1)

  def test_get_house(self):
    self.assertEqual(self.db.get_house('Arya Stark'), 'Stark')
    self.assertEqual(self.db.get_house('Cersei Lannister'), 'Lannister')
    self.assertEqual(self.db.get_house('not a character'), -1)

  def test_get_birth_year(self):
    self.assertEqual(self.db.get_birth_year('Arya Stark'), 289)
    self.assertEqual(self.db.get_birth_year('Drogo'), 267)
    self.assertEqual(self.db.get_birth_year('not a character'), -1)

  def test_get_death_year(self):
    self.assertEqual(self.db.get_death_year('Arya Stark'), '')
    self.assertEqual(self.db.get_death_year('Drogo'), 298)
    self.assertEqual(self.db.get_death_year('not a character'), -1)

  def test_get_death_book(self):
    self.assertEqual(self.db.get_death_book('Jon Snow'), '')
    self.assertEqual(self.db.get_death_book('Drogo'), 1)
    self.assertEqual(self.db.get_death_book('not a character'), -1)

  def test_get_intro_book(self):
    self.assertEqual(self.db.get_intro_book('Arya Stark'), 1)
    self.assertEqual(self.db.get_intro_book('Ramsay Snow'), 2)
    self.assertEqual(self.db.get_intro_book('Eddard Stark'), 1)


  def test_get_death_chapter(self):
    self.assertEqual(self.db.get_death_chapter('Jon Snow'), '')
    self.assertEqual(self.db.get_death_chapter('Drogo'), 64)
    self.assertEqual(self.db.get_death_chapter('not a character'), -1)

  def test_get_intro_chapter(self):
    self.assertEqual(self.db.get_intro_chapter('Jon Snow'), 1)
    self.assertEqual(self.db.get_intro_chapter('Margaery Tyrell'), 22)
    self.assertEqual(self.db.get_intro_chapter('not a character'), -1)

  def test_get_title(self):
    self.assertEqual(self.db.get_title('Quentin Tyrell'), "Ser")
    self.assertEqual(self.db.get_title('Margaery Tyrell'), "Seven Kingdoms")
    self.assertEqual(self.db.get_title('not a character'), -1)

  def test_get_book_deaths(self):
    self.assertTrue('Eddard Stark' in self.db.get_book_deaths(1))
    self.assertTrue('Joffrey Baratheon' in self.db.get_book_deaths(3))
    self.assertTrue('Arya Stark' not in self.db.get_book_deaths(4))

if __name__ == '__main__':
  unittest.main()
