#!/usr/bin/env python
import unittest
from object_depth.main import is_a_class_object, object_depth_checker

class Person(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address


class Address(object):
    def __init__(self, geo_location, address):
        self.geo_location = geo_location
        self.address = address


class ObjectDepthChecker(unittest.TestCase):

    def setUp(self):
        super(ObjectDepthChecker, self).setUp()
        self.address = Address((23.0000, 90.000), 'Dhaka, Bangladesh')
        self.person = Person('Aanisha', self.address)

        self.dictionary = {
            'this': 1,
            'is': {
                'a': {
                    'dictionary': {
                        'person': self.person
                    }
                }
            },
            '.': 'Good Luck'
        }

    def test_is_a_class_object(self):
        self.assertEqual(is_a_class_object('This is string'), False)
        self.assertEqual(is_a_class_object(self.person), True)

    def test_object_depth_checker(self):
        _test1 = object_depth_checker(self.dictionary)
        _test2 = object_depth_checker(self.person)

        self.assertEqual(_test1, None)
        self.assertEqual(_test2[0], False)
        self.assertEqual(_test2[1], 'Expected Dictionary.')