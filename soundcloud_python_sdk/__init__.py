# coding: utf-8

# flake8: noqa

"""
    SoundCloud Public API Specification

    Discover and play over 320 million music tracks. Join the world’s largest online community of artists, bands, DJs, and audio creators.

    The version of the OpenAPI document: 1.0.0
    Created by: https://github.com/soundcloud/api
"""

__version__ = "1.0.0"

# import ApiClient
from soundcloud_python_sdk.api_client import ApiClient

# import Configuration
from soundcloud_python_sdk.configuration import Configuration

# import exceptions
from soundcloud_python_sdk.exceptions import OpenApiException
from soundcloud_python_sdk.exceptions import ApiAttributeError
from soundcloud_python_sdk.exceptions import ApiTypeError
from soundcloud_python_sdk.exceptions import ApiValueError
from soundcloud_python_sdk.exceptions import ApiKeyError
from soundcloud_python_sdk.exceptions import ApiException

from soundcloud_python_sdk.client import SoundCloud
