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


class CommentUser(BaseModel):
    # unique identifier
    id: typing.Optional[int] = Field(None, alias='id')

    # kind of resource.
    kind: typing.Optional[str] = Field(None, alias='kind')

    # permalink of the resource.
    permalink: typing.Optional[str] = Field(None, alias='permalink')

    # username
    username: typing.Optional[str] = Field(None, alias='username')

    # last modified timestamp.
    last_modified: typing.Optional[str] = Field(None, alias='last_modified')

    # API resource URL.
    uri: typing.Optional[str] = Field(None, alias='uri')

    # URL to the SoundCloud.com page.
    permalink_url: typing.Optional[str] = Field(None, alias='permalink_url')

    # URL to a JPEG image.
    avatar_url: typing.Optional[str] = Field(None, alias='avatar_url')

    # number of followers.
    followers_count: typing.Optional[int] = Field(None, alias='followers_count')

    # number of followed users.
    followings_count: typing.Optional[int] = Field(None, alias='followings_count')

    # number of reposts from user
    reposts_count: typing.Optional[int] = Field(None, alias='reposts_count')
    class Config:
        arbitrary_types_allowed = True
