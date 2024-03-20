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


class RequiredWebProfilesItem(TypedDict):
    pass

class OptionalWebProfilesItem(TypedDict, total=False):
    # Link's title
    title: str

    # Timestamp of when the link was added to the profile.
    created_at: str

    # Id
    id: int

    # Kind
    kind: str

    # Service or platform
    service: str

    # URL of the external link
    url: str

    # Username extracted from the external link
    username: str

class WebProfilesItem(RequiredWebProfilesItem, OptionalWebProfilesItem):
    pass
