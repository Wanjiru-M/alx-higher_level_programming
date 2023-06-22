#!/usr/bin/python3
"""Unit test class Rectangle"""
import unittest
import json
import sys
import os
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def setUp(self):
        """Set up test fixtures"""

        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)

    def tearDown(self):
        """Clean up test fixtures"""

        del self.r1
        del self.r2
        del self.r3

    def test_instance(self):
        """Test instance creation"""

        self.assertIsInstance(self.r1, Rectangle)
        self.assertIsInstance(self.r2, Rectangle)
        self.assertIsInstance(self.r3, Rectangle)

    def test_attributes(self):
        """Test instance attributes"""

        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)

        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r2.y, 0)

        self.assertEqual(self.r3.width, 10)
        self.assertEqual(self.r3.height, 2)
        self.assertEqual(self.r3.x, 0)
        self.assertEqual(self.r3.y, 0)
        self.assertEqual(self.r3.id, 12)

    def test_update_attributes(self):
        """Test update attributes"""

        self.r1.update(4, 6, 2, 1, 15)
        self.assertEqual(self.r1.width, 4)
        self.assertEqual(self.r1.height, 6)
        self.assertEqual(self.r1.x, 2)
        self.assertEqual(self.r1.y, 1)
        self.assertEqual(self.r1.id, 15)

    def test_to_dictionary(self):
        """Test to_dictionary method"""

        expected_dict = {
            'id': 1,
            'width': 10,
            'height': 2,
            'x': 0,
            'y': 0
        }
        self.assertEqual(self.r1.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
