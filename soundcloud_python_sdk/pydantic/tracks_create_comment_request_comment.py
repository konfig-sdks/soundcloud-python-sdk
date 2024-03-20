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


class TracksCreateCommentRequestComment(BaseModel):
    # Comment's content
    body: str = Field(alias='body')

    # Timestamp of a comment. String or float representation is supported
    timestamp: typing.Optional[typing.Union[str, typing.Union[int, float]]] = Field(None, alias='timestamp')
    class Config:
        arbitrary_types_allowed = True
