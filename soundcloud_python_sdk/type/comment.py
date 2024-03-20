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

from soundcloud_python_sdk.type.comment_user import CommentUser

class RequiredComment(TypedDict):
    pass

class OptionalComment(TypedDict, total=False):
    # Comment body.
    body: str

    # Created timestamp.
    created_at: str

    # Identifier.
    id: int

    # Kind (comment).
    kind: str

    # User's identifier.
    user_id: int

    # Timestamp.
    timestamp: str

    # Track's identifier.
    track_id: int

    # Comment's URL.
    uri: str

    user: CommentUser

class Comment(RequiredComment, OptionalComment):
    pass
