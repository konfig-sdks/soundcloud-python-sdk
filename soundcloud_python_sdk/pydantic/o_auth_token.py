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
from pydantic import BaseModel, Field, RootModel


class OAuthToken(BaseModel):
    # One of `authorization_code`, `client_credentials`, `refresh_token`
    grant_type: Literal["authorization_code", "refresh_token", "client_credentials"] = Field(alias='grant_type')

    # Client ID
    client_id: str = Field(alias='client_id')

    # Client secret
    client_secret: str = Field(alias='client_secret')

    # Authorization code. Required on `grant_type = authorization_code`.
    code: typing.Optional[str] = Field(None, alias='code')

    # Redirect URI. Required on `grant_type = (authorization_code|refresh_token)`.
    redirect_uri: typing.Optional[str] = Field(None, alias='redirect_uri')

    # Refresh token. Required on `grant_type = refresh_token`.
    refresh_token: typing.Optional[str] = Field(None, alias='refresh_token')
    class Config:
        arbitrary_types_allowed = True
