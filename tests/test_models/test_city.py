#!/usr/bin/env python3
"""
    test from basemodel
"""
import unittest
import os
from models.city import City


class TestCity(unittest.TestCase):
    """
    test city
    """

    def setUp(self):
        """setup"""
        if not os.path.exists("file.json"):
            os.mknod("file.json")
        self.city = City()

    def tearDown(self):
        """tear down"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        del self.city

    def test_creation(self):
        '''
        ensure correct creation
        '''
        self.assertEqual(self.city.name, '')
        self.assertEqual(self.city.state_id, '')
