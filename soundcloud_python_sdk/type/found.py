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


class RequiredFound(TypedDict):
    pass

class OptionalFound(TypedDict, total=False):
    # Status code.
    status: str

    # Location URL of the resource.
    location: str

class Found(RequiredFound, OptionalFound):
    pass
