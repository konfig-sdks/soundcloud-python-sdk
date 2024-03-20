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

from soundcloud_python_sdk.type.track import Track
from soundcloud_python_sdk.type.user import User

class RequiredPlaylist(TypedDict):
    pass

class OptionalPlaylist(TypedDict, total=False):
    # Tags.
    tags: typing.Optional[str]

    # Playlist title.
    title: str

    # Playlist description.
    description: str

    # Playlist identifier.
    id: int

    # Type of Soundcloud object (playlist).
    kind: str

    # URL to a JPEG image.
    artwork_url: str

    # Created timestamp.
    created_at: str

    # is downloadable.
    downloadable: bool

    # Playlist duration.
    duration: int

    # European Article Number.
    ean: str

    # Embeddable by.
    embeddable_by: str

    # Playlist genre.
    genre: str

    # Label user identifier.
    label_id: int

    # Label name.
    label_name: str

    # Last modified timestamp.
    last_modified: str

    # License.
    license: str

    # Playlist permalink.
    permalink: str

    # Playlist permalink URL.
    permalink_url: str

    # Type of playlist.
    playlist_type: str

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

    # Type of sharing (private/public).
    sharing: str

    # Is streamable.
    streamable: bool

    # Tags.
    tag_list: str

    # Count of tracks.
    track_count: int

    # List of tracks.
    tracks: typing.List[Track]

    # Playlist type.
    type: str

    # Playlist URI.
    uri: str

    user: User

    # User identifier.
    user_id: int

    # Count of playlist likes.
    likes_count: int

    label: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # tracks URI.
    tracks_uri: typing.Optional[str]

class Playlist(RequiredPlaylist, OptionalPlaylist):
    pass
