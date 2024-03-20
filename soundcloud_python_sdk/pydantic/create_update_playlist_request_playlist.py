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

from soundcloud_python_sdk.pydantic.create_update_playlist_request_playlist_tracks import CreateUpdatePlaylistRequestPlaylistTracks

class CreateUpdatePlaylistRequestPlaylist(BaseModel):
    # Title of the playlist
    title: typing.Optional[str] = Field(None, alias='title')

    # Description of the playlist
    description: typing.Optional[str] = Field(None, alias='description')

    # public or private
    sharing: typing.Optional[Literal["public", "private"]] = Field(None, alias='sharing')

    tracks: typing.Optional[CreateUpdatePlaylistRequestPlaylistTracks] = Field(None, alias='tracks')

    artwork_data: typing.Optional[typing.IO] = Field(None, alias='artwork_data')

    # The European Article Number
    ean: typing.Optional[str] = Field(None, alias='ean')

    # Playlist's genre
    genre: typing.Optional[str] = Field(None, alias='genre')

    # Label name
    label_name: typing.Optional[str] = Field(None, alias='label_name')

    # License number
    license: typing.Optional[str] = Field(None, alias='license')

    # Playlist's permalink
    permalink: typing.Optional[str] = Field(None, alias='permalink')

    # Full permalink URL
    permalink_url: typing.Optional[str] = Field(None, alias='permalink_url')

    # Purchase title
    purchase_title: typing.Optional[str] = Field(None, alias='purchase_title')

    # Purchase URL
    purchase_url: typing.Optional[str] = Field(None, alias='purchase_url')

    # Playlist's release
    release: typing.Optional[str] = Field(None, alias='release')

    # Release date
    release_date: typing.Optional[str] = Field(None, alias='release_date')

    # Playlist or album type
    set_type: typing.Optional[Literal["album", "playlist"]] = Field(None, alias='set_type')

    # A comma-separated list of tags
    tag_list: typing.Optional[str] = Field(None, alias='tag_list')
    class Config:
        arbitrary_types_allowed = True
