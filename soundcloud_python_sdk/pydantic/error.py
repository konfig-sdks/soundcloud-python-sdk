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

from soundcloud_python_sdk.pydantic.error_errors import ErrorErrors

class Error(BaseModel):
    code: typing.Optional[int] = Field(None, alias='code')

    message: typing.Optional[str] = Field(None, alias='message')

    link: typing.Optional[str] = Field(None, alias='link')

    error: typing.Optional[typing.Optional[str]] = Field(None, alias='error')

    errors: typing.Optional[ErrorErrors] = Field(None, alias='errors')

    status: typing.Optional[str] = Field(None, alias='status')
    class Config:
        arbitrary_types_allowed = True
