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

from soundcloud_python_sdk.pydantic.user import User

class Track(BaseModel):
    # Track title.
    title: typing.Optional[str] = Field(None, alias='title')

    # Track description.
    description: typing.Optional[str] = Field(None, alias='description')

    # URL to a JPEG image.
    artwork_url: typing.Optional[str] = Field(None, alias='artwork_url')

    # Tempo.
    bpm: typing.Optional[int] = Field(None, alias='bpm')

    # Number of comments.
    comment_count: typing.Optional[int] = Field(None, alias='comment_count')

    # Is commentable.
    commentable: typing.Optional[bool] = Field(None, alias='commentable')

    # Created timestamp.
    created_at: typing.Optional[str] = Field(None, alias='created_at')

    # NUmber of downloads.
    download_count: typing.Optional[int] = Field(None, alias='download_count')

    # Is downloadable.
    downloadable: typing.Optional[str] = Field(None, alias='downloadable')

    # Track duration.
    duration: typing.Optional[int] = Field(None, alias='duration')

    # Embeddable by.
    embeddable_by: typing.Optional[str] = Field(None, alias='embeddable_by')

    # Number of favoritings.
    favoritings_count: typing.Optional[int] = Field(None, alias='favoritings_count')

    # Genre
    genre: typing.Optional[str] = Field(None, alias='genre')

    # Track identifier.
    id: typing.Optional[int] = Field(None, alias='id')

    # ISRC code.
    isrc: typing.Optional[str] = Field(None, alias='isrc')

    # Key signature.
    key_signature: typing.Optional[str] = Field(None, alias='key_signature')

    # Type of object (track).
    kind: typing.Optional[str] = Field(None, alias='kind')

    # Label user name.
    label_name: typing.Optional[str] = Field(None, alias='label_name')

    # License
    license: typing.Optional[str] = Field(None, alias='license')

    # Permalink URL.
    permalink_url: typing.Optional[str] = Field(None, alias='permalink_url')

    # Number of plays.
    playback_count: typing.Optional[int] = Field(None, alias='playback_count')

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

    # Type of sharing (public/private).
    sharing: typing.Optional[str] = Field(None, alias='sharing')

    # URL to stream.
    stream_url: typing.Optional[str] = Field(None, alias='stream_url')

    # Is streamable.
    streamable: typing.Optional[bool] = Field(None, alias='streamable')

    # Tags.
    tag_list: typing.Optional[str] = Field(None, alias='tag_list')

    # Track URI.
    uri: typing.Optional[str] = Field(None, alias='uri')

    user: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='user')

    # Is user's favourite.
    user_favorite: typing.Optional[bool] = Field(None, alias='user_favorite')

    # Number of plays by a user.
    user_playback_count: typing.Optional[int] = Field(None, alias='user_playback_count')

    # Waveform URL.
    waveform_url: typing.Optional[str] = Field(None, alias='waveform_url')

    # List of countries where track is available.
    available_country_codes: typing.Optional[str] = Field(None, alias='available_country_codes')

    # Level of access the user (logged in or anonymous) has to the track.   * `playable` - user is allowed to listen to a full track.   * `preview` - user is allowed to preview a track, meaning a snippet is available   * `blocked` - user can only see the metadata of a track, no streaming is possible 
    access: typing.Optional[Literal["playable", "preview", "blocked"]] = Field(None, alias='access')

    # URL to download a track.
    download_url: typing.Optional[str] = Field(None, alias='download_url')

    # Number of reposts.
    reposts_count: typing.Optional[int] = Field(None, alias='reposts_count')

    # Secret URL.
    secret_uri: typing.Optional[str] = Field(None, alias='secret_uri')
    class Config:
        arbitrary_types_allowed = True
