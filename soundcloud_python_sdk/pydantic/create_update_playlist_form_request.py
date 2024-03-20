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


class CreateUpdatePlaylistFormRequest(BaseModel):
    playlist[title]_: typing.Optional[str] = Field(None, alias='playlist[title]')

    playlist[sharing]_: typing.Optional[Literal["public", "private"]] = Field(None, alias='playlist[sharing]')

    playlist[description]_: typing.Optional[str] = Field(None, alias='playlist[description]')

    # To pass multiple tracks, pass multiple comma-separated values, e.g. -F \"playlist[tracks][][id]=111,222\"
    playlist[tracks][][id]_: typing.Optional[str] = Field(None, alias='playlist[tracks][][id]')

    playlist[artwork_data]_: typing.Optional[typing.IO] = Field(None, alias='playlist[artwork_data]')

    playlist[ean]_: typing.Optional[str] = Field(None, alias='playlist[ean]')

    playlist[genre]_: typing.Optional[str] = Field(None, alias='playlist[genre]')

    playlist[label_name]_: typing.Optional[str] = Field(None, alias='playlist[label_name]')

    playlist[license]_: typing.Optional[str] = Field(None, alias='playlist[license]')

    playlist[permalink]_: typing.Optional[str] = Field(None, alias='playlist[permalink]')

    playlist[permalink_url]_: typing.Optional[str] = Field(None, alias='playlist[permalink_url]')

    playlist[purchase_title]_: typing.Optional[str] = Field(None, alias='playlist[purchase_title]')

    playlist[purchase_url]_: typing.Optional[str] = Field(None, alias='playlist[purchase_url]')

    playlist[release]_: typing.Optional[str] = Field(None, alias='playlist[release]')

    playlist[release_date]_: typing.Optional[str] = Field(None, alias='playlist[release_date]')

    playlist[set_type]_: typing.Optional[Literal["album", "playlist"]] = Field(None, alias='playlist[set_type]')

    playlist[tag_list]_: typing.Optional[str] = Field(None, alias='playlist[tag_list]')
    class Config:
        arbitrary_types_allowed = True
