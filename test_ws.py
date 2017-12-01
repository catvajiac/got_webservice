#!/usr/bin/env python3

import unittest
import requests
import json


class TestServer(unittest.TestCase):
  port = '7000'
  print("Testing on port {}".format(port))
  #url = 'http://student04.cse.nd.edu:{}'.format(port)
  url = 'http://localhost:{}'.format(port)

  def is_json(self, response):
    try:
      json.loads(response)
      return True
    except ValueError:
      return False

  def test_get_characters(self):
    r = requests.get('{}/characters/'.format(self.url))
    self.assertTrue(self.is_json(r.content))

    response = json.loads(r.content)
    self.assertEqual(response['result'], 'success')
    self.assertTrue('Arya Stark' in response['names'])
    self.assertTrue('Jon Snow' in response['names'])
    self.assertTrue('not a character' not in response['names'])

  def test_get_character(self):
    r = requests.get('{}/characters/Arya_Stark'.format(self.url))
    self.assertTrue(self.is_json(r.content))

    response = json.loads(r.content)
    self.assertEqual(response['result'], 'success')
    self.assertEqual(response['num_dead_relations'], 8)
    self.assertEqual(response['house'], 'House Stark')

  def test_get_houses(self):
    r = requests.get('{}/houses/'.format(self.url))
    self.assertTrue(self.is_json(r.content))

    response = json.loads(r.content)
    self.assertEqual(response['result'], 'success')
    self.assertTrue('Targaryen' in response['houses'])
    self.assertTrue('Stark' in response['houses'])
    self.assertTrue('not a house' not in response['houses'])

  def test_get_house(self):
    r = requests.get('{}/houses/Stark'.format(self.url))
    self.assertTrue(self.is_json(r.content))

    response = json.loads(r.content)
    self.assertEqual(response['result'], 'success')
    self.assertTrue('Arya Stark' in response['names'])
    self.assertTrue('Eddard Stark' in response['names'])
    self.assertTrue('not a Stark' not in response['names'])

  def test_get_dead(self):
    r = requests.get('{}/dead/'.format(self.url))
    self.assertTrue(self.is_json(r.content))

    response = json.loads(r.content)
    self.assertEqual(response['result'], 'success')
    self.assertTrue('Eddard Stark' in response['dead'])
    self.assertTrue('Joffrey Baratheon' in response['dead'])
    self.assertTrue('Arya Stark' not in response['dead'])

  def test_get_dead_book(self):
    r = requests.get('{}/dead/1'.format(self.url))
    self.assertTrue(self.is_json(r.content))

    response = json.loads(r.content)
    self.assertEqual(response['result'], 'success')
    self.assertTrue('Eddard Stark' in response['dead'])
    self.assertTrue('Drogo' in response['dead'])
    self.assertTrue('Dale Seaworth' not in response['dead'])

  def test_get_bookstats(self):
    r = requests.get('{}/bookstats/'.format(self.url))
    self.assertTrue(self.is_json(r.content))

    response = json.loads(r.content)
    self.assertEqual(response['result'], 'success')
    self.assertEqual(response[1]['num_deaths'], 47)
    self.assertTrue('Drogo' in response[1]['dead'])
    self.assertTrue('Eddard Stark' in response[1]['dead'])
    self.assertTrue('not a character' not in response[1]['dead'])

  def test_get_bookstats(self):
    r = requests.get('{}/bookstats/1'.format(self.url))
    self.assertTrue(self.is_json(r.content))

    response = json.loads(r.content)
    self.assertEqual(response['result'], 'success')
    self.assertEqual(response['num_deaths'], 47)
    self.assertTrue('Drogo' in response['dead'])
    self.assertTrue('Eddard Stark' in response['dead'])
    self.assertTrue('not a character' not in response['dead'])

if __name__ == "__main__":
  unittest.main()
