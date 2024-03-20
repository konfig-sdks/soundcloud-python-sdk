# coding: utf-8

"""
    SoundCloud Public API Specification

    Discover and play over 320 million music tracks. Join the world’s largest online community of artists, bands, DJs, and audio creators.

    The version of the OpenAPI document: 1.0.0
    Created by: https://github.com/soundcloud/api
"""

import unittest

import os
from pprint import pprint
from soundcloud_python_sdk import SoundCloud

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        soundcloud = SoundCloud(
        
                        auth_header = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(soundcloud)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
