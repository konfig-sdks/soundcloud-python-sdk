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

from soundcloud_python_sdk.pydantic.track import Track
from soundcloud_python_sdk.pydantic.user import User

class Playlist(BaseModel):
    # Tags.
    tags: typing.Optional[typing.Optional[str]] = Field(None, alias='tags')

    # Playlist title.
    title: typing.Optional[str] = Field(None, alias='title')

    # Playlist description.
    description: typing.Optional[str] = Field(None, alias='description')

    # Playlist identifier.
    id: typing.Optional[int] = Field(None, alias='id')

    # Type of Soundcloud object (playlist).
    kind: typing.Optional[str] = Field(None, alias='kind')

    # URL to a JPEG image.
    artwork_url: typing.Optional[str] = Field(None, alias='artwork_url')

    # Created timestamp.
    created_at: typing.Optional[str] = Field(None, alias='created_at')

    # is downloadable.
    downloadable: typing.Optional[bool] = Field(None, alias='downloadable')

    # Playlist duration.
    duration: typing.Optional[int] = Field(None, alias='duration')

    # European Article Number.
    ean: typing.Optional[str] = Field(None, alias='ean')

    # Embeddable by.
    embeddable_by: typing.Optional[str] = Field(None, alias='embeddable_by')

    # Playlist genre.
    genre: typing.Optional[str] = Field(None, alias='genre')

    # Label user identifier.
    label_id: typing.Optional[int] = Field(None, alias='label_id')

    # Label name.
    label_name: typing.Optional[str] = Field(None, alias='label_name')

    # Last modified timestamp.
    last_modified: typing.Optional[str] = Field(None, alias='last_modified')

    # License.
    license: typing.Optional[str] = Field(None, alias='license')

    # Playlist permalink.
    permalink: typing.Optional[str] = Field(None, alias='permalink')

    # Playlist permalink URL.
    permalink_url: typing.Optional[str] = Field(None, alias='permalink_url')

    # Type of playlist.
    playlist_type: typing.Optional[str] = Field(None, alias='playlist_type')

    # Purchase title.
    purchase_title: typing.Optional[str] = Field(None, alias='purchase_title')

    # Purchase URL.
    purchase_url: typing.Optional[str] = Field(None, alias='purchase_url')

    # Release.
    release: typing.Optional[str] = Field(None, alias='release')

    # Day of release.
    release_day: typing.Optional[int] = Field(None, alias='release_day')

    # Month of release.
    release_month: typing.Optional[int] = Field(None, alias='release_month')

    # Year of release.
    release_year: typing.Optional[int] = Field(None, alias='release_year')

    # Type of sharing (private/public).
    sharing: typing.Optional[str] = Field(None, alias='sharing')

    # Is streamable.
    streamable: typing.Optional[bool] = Field(None, alias='streamable')

    # Tags.
    tag_list: typing.Optional[str] = Field(None, alias='tag_list')

    # Count of tracks.
    track_count: typing.Optional[int] = Field(None, alias='track_count')

    # List of tracks.
    tracks: typing.Optional[typing.List[Track]] = Field(None, alias='tracks')

    # Playlist type.
    type: typing.Optional[str] = Field(None, alias='type')

    # Playlist URI.
    uri: typing.Optional[str] = Field(None, alias='uri')

    user: typing.Optional[User] = Field(None, alias='user')

    # User identifier.
    user_id: typing.Optional[int] = Field(None, alias='user_id')

    # Count of playlist likes.
    likes_count: typing.Optional[int] = Field(None, alias='likes_count')

    label: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='label')

    # tracks URI.
    tracks_uri: typing.Optional[typing.Optional[str]] = Field(None, alias='tracks_uri')
    class Config:
        arbitrary_types_allowed = True
