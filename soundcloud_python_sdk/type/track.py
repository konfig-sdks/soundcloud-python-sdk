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

from soundcloud_python_sdk.type.user import User

class RequiredTrack(TypedDict):
    pass

class OptionalTrack(TypedDict, total=False):
    # Track title.
    title: str

    # Track description.
    description: str

    # URL to a JPEG image.
    artwork_url: str

    # Tempo.
    bpm: int

    # Number of comments.
    comment_count: int

    # Is commentable.
    commentable: bool

    # Created timestamp.
    created_at: str

    # NUmber of downloads.
    download_count: int

    # Is downloadable.
    downloadable: str

    # Track duration.
    duration: int

    # Embeddable by.
    embeddable_by: str

    # Number of favoritings.
    favoritings_count: int

    # Genre
    genre: str

    # Track identifier.
    id: int

    # ISRC code.
    isrc: str

    # Key signature.
    key_signature: str

    # Type of object (track).
    kind: str

    # Label user name.
    label_name: str

    # License
    license: str

    # Permalink URL.
    permalink_url: str

    # Number of plays.
    playback_count: int

    # Purchase title.
    purchase_title: str

    # Purchase URL.
    purchase_url: str

    # Release.
    release: str

    # Day of release.
    release_day: int

    # Month of release.
    release_month: int

    # Year of release.
    release_year: int

    # Type of sharing (public/private).
    sharing: str

    # URL to stream.
    stream_url: str

    # Is streamable.
    streamable: bool

    # Tags.
    tag_list: str

    # Track URI.
    uri: str

    user: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Is user's favourite.
    user_favorite: bool

    # Number of plays by a user.
    user_playback_count: int

    # Waveform URL.
    waveform_url: str

    # List of countries where track is available.
    available_country_codes: str

    # Level of access the user (logged in or anonymous) has to the track.   * `playable` - user is allowed to listen to a full track.   * `preview` - user is allowed to preview a track, meaning a snippet is available   * `blocked` - user can only see the metadata of a track, no streaming is possible 
    access: typing.Optional[str]

    # URL to download a track.
    download_url: str

    # Number of reposts.
    reposts_count: int

    # Secret URL.
    secret_uri: str

class Track(RequiredTrack, OptionalTrack):
    pass
