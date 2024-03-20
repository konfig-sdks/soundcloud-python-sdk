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
from soundcloud_python_sdk.paths.oauth2_token import post
from soundcloud_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestOauth2Token(ApiTestMixin, unittest.TestCase):
    """
    Oauth2Token unit test stubs
        This endpoint accepts POST requests and is used to provision access tokens once a user has authorized your application.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200








if __name__ == '__main__':
    unittest.main()
