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

from soundcloud_python_sdk.pydantic.activities_collection_item_origin import ActivitiesCollectionItemOrigin

class ActivitiesCollectionItem(BaseModel):
    # Type of activity (track).
    type: typing.Optional[str] = Field(None, alias='type')

    # Created timestamp.
    created_at: typing.Optional[str] = Field(None, alias='created_at')

    origin: typing.Optional[ActivitiesCollectionItemOrigin] = Field(None, alias='origin')
    class Config:
        arbitrary_types_allowed = True
