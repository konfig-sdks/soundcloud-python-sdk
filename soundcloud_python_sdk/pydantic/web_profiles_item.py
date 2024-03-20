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


class WebProfilesItem(BaseModel):
    # Link's title
    title: typing.Optional[str] = Field(None, alias='title')

    # Timestamp of when the link was added to the profile.
    created_at: typing.Optional[str] = Field(None, alias='created_at')

    # Id
    id: typing.Optional[int] = Field(None, alias='id')

    # Kind
    kind: typing.Optional[str] = Field(None, alias='kind')

    # Service or platform
    service: typing.Optional[str] = Field(None, alias='service')

    # URL of the external link
    url: typing.Optional[str] = Field(None, alias='url')

    # Username extracted from the external link
    username: typing.Optional[str] = Field(None, alias='username')
    class Config:
        arbitrary_types_allowed = True
