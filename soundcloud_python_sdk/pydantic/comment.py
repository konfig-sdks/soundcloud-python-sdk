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

from soundcloud_python_sdk.pydantic.comment_user import CommentUser

class Comment(BaseModel):
    # Comment body.
    body: typing.Optional[str] = Field(None, alias='body')

    # Created timestamp.
    created_at: typing.Optional[str] = Field(None, alias='created_at')

    # Identifier.
    id: typing.Optional[int] = Field(None, alias='id')

    # Kind (comment).
    kind: typing.Optional[str] = Field(None, alias='kind')

    # User's identifier.
    user_id: typing.Optional[int] = Field(None, alias='user_id')

    # Timestamp.
    timestamp: typing.Optional[str] = Field(None, alias='timestamp')

    # Track's identifier.
    track_id: typing.Optional[int] = Field(None, alias='track_id')

    # Comment's URL.
    uri: typing.Optional[str] = Field(None, alias='uri')

    user: typing.Optional[CommentUser] = Field(None, alias='user')
    class Config:
        arbitrary_types_allowed = True
