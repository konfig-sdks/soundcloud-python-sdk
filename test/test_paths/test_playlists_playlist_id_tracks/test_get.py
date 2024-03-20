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
from soundcloud_python_sdk.paths.playlists_playlist_id_tracks import get
from soundcloud_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestPlaylistsPlaylistIdTracks(ApiTestMixin, unittest.TestCase):
    """
    PlaylistsPlaylistIdTracks unit test stubs
        Returns tracks under a playlist.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
