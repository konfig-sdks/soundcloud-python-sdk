# coding: utf-8

"""
    SoundCloud Public API Specification

    Discover and play over 320 million music tracks. Join the world’s largest online community of artists, bands, DJs, and audio creators.

    The version of the OpenAPI document: 1.0.0
    Created by: https://github.com/soundcloud/api
"""

import unittest
from unittest.mock import patch

import urllib3

import soundcloud_python_sdk
from soundcloud_python_sdk.paths.tracks_track_id_related import get
from soundcloud_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestTracksTrackIdRelated(ApiTestMixin, unittest.TestCase):
    """
    TracksTrackIdRelated unit test stubs
        Returns all related tracks of track on SoundCloud.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
