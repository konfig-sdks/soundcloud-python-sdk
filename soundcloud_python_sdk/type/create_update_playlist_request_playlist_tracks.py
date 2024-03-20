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

from soundcloud_python_sdk.type.create_update_playlist_request_playlist_tracks_item import CreateUpdatePlaylistRequestPlaylistTracksItem

CreateUpdatePlaylistRequestPlaylistTracks = typing.List[CreateUpdatePlaylistRequestPlaylistTracksItem]
