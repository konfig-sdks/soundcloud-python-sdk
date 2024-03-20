# coding: utf-8

"""
    SoundCloud Public API Specification

    Discover and play over 320 million music tracks. Join the world’s largest online community of artists, bands, DJs, and audio creators.

    The version of the OpenAPI document: 1.0.0
    Created by: https://github.com/soundcloud/api
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredOAuthToken(TypedDict):
    # One of `authorization_code`, `client_credentials`, `refresh_token`
    grant_type: str

    # Client ID
    client_id: str

    # Client secret
    client_secret: str

class OptionalOAuthToken(TypedDict, total=False):
    # Authorization code. Required on `grant_type = authorization_code`.
    code: str

    # Redirect URI. Required on `grant_type = (authorization_code|refresh_token)`.
    redirect_uri: str

    # Refresh token. Required on `grant_type = refresh_token`.
    refresh_token: str

class OAuthToken(RequiredOAuthToken, OptionalOAuthToken):
    pass
