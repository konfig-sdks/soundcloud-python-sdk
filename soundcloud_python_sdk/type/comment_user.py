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


class RequiredCommentUser(TypedDict):
    pass

class OptionalCommentUser(TypedDict, total=False):
    # unique identifier
    id: int

    # kind of resource.
    kind: str

    # permalink of the resource.
    permalink: str

    # username
    username: str

    # last modified timestamp.
    last_modified: str

    # API resource URL.
    uri: str

    # URL to the SoundCloud.com page.
    permalink_url: str

    # URL to a JPEG image.
    avatar_url: str

    # number of followers.
    followers_count: int

    # number of followed users.
    followings_count: int

    # number of reposts from user
    reposts_count: int

class CommentUser(RequiredCommentUser, OptionalCommentUser):
    pass
