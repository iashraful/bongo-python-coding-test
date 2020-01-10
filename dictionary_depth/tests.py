#!/usr/bin/env python
import unittest
from dictionary_depth.main import has_next_label, depth_checker

class DictionaryDepthChecker(unittest.TestCase):

    def setUp(self):
        super(DictionaryDepthChecker, self).setUp()

        self.test_1_dict = {
            'name': 'Ashraful',
            'Test_1': 'Test 1',
            'Test_2': {
                'Test_3': {
                    'Test_4': 'Nothing'
                }
            }
        }
        self.test_2_non_dict = [1, 2, 3, 4]

    def test_has_next_level(self):
        self.assertEqual(has_next_label("this is not a dictionary"), False)
        self.assertEqual(has_next_label(self.test_2_non_dict), False)
        self.assertEqual(has_next_label(self.test_1_dict), True)

    def test_depth_checker(self):
        test_1 = depth_checker(self.test_1_dict)
        test_2 = depth_checker(self.test_2_non_dict)

        self.assertEqual(test_1, None)
        self.assertEqual(test_2[0], False)
        self.assertEqual(test_2[1], 'Expected Dictionary.')
