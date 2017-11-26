#!/usr/bin/env python2.7

import _got_database
import unittest

class DatabaseUtils(unittest.TestCase):
  db = _got_database._got_database()
  db.load_files(dir="data")

  def test_dead(self):
    self.assertEqual(self.db.is_dead('Elwood'), False)
    self.assertEqual(self.db.is_dead('Jate Blackberry'), True)
    self.assertEqual(self.db.is_dead('not a character'), -1)

if __name__ == '__main__':
  unittest.main()
