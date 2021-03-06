#!/usr/bin/env python

import sys
import unittest

sys.path.append('../')
import combatwiz_runner as mod

class Test_get_distance(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_different_places(self):
        self.assertTrue(mod.get_distance([0,0], [10,10]) > 1)

    def test_same_place(self):
        self.assertTrue(mod.get_distance([0,0], [0,0]) == 0)

    def test_distance(self):
        self.assertTrue(int(mod.get_distance([10,5], [6,12])) == 8)

    def test_negative_coordinates(self):
        self.assertRaises(AssertionError, mod.get_distance, [0,0], [-10,-10])

    def test_different_places(self):
        self.assertEqual(mod.get_distance([60,60], [60,68]), 8)
        self.assertEqual(mod.get_distance([60,60], [60.0,68]), 8)

if __name__ == "__main__":
    unittest.main()
