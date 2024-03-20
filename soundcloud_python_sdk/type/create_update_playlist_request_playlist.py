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

from soundcloud_python_sdk.type.create_update_playlist_request_playlist_tracks import CreateUpdatePlaylistRequestPlaylistTracks

class RequiredCreateUpdatePlaylistRequestPlaylist(TypedDict):
    pass

class OptionalCreateUpdatePlaylistRequestPlaylist(TypedDict, total=False):
    # Title of the playlist
    title: str

    # Description of the playlist
    description: str

    # public or private
    sharing: str

    tracks: CreateUpdatePlaylistRequestPlaylistTracks

    artwork_data: typing.IO

    # The European Article Number
    ean: str

    # Playlist's genre
    genre: str

    # Label name
    label_name: str

    # License number
    license: str

    # Playlist's permalink
    permalink: str

    # Full permalink URL
    permalink_url: str

    # Purchase title
    purchase_title: str

    # Purchase URL
    purchase_url: str

    # Playlist's release
    release: str

    # Release date
    release_date: str

    # Playlist or album type
    set_type: str

    # A comma-separated list of tags
    tag_list: str

class CreateUpdatePlaylistRequestPlaylist(RequiredCreateUpdatePlaylistRequestPlaylist, OptionalCreateUpdatePlaylistRequestPlaylist):
    pass
