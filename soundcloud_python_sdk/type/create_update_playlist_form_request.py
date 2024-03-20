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


RequiredCreateUpdatePlaylistFormRequest = TypedDict("RequiredCreateUpdatePlaylistFormRequest", {
    })

OptionalCreateUpdatePlaylistFormRequest = TypedDict("OptionalCreateUpdatePlaylistFormRequest", {
    "playlist[title]": str,

    "playlist[sharing]": str,

    "playlist[description]": str,

    # To pass multiple tracks, pass multiple comma-separated values, e.g. -F \"playlist[tracks][][id]=111,222\"
    "playlist[tracks][][id]": str,

    "playlist[artwork_data]": typing.IO,

    "playlist[ean]": str,

    "playlist[genre]": str,

    "playlist[label_name]": str,

    "playlist[license]": str,

    "playlist[permalink]": str,

    "playlist[permalink_url]": str,

    "playlist[purchase_title]": str,

    "playlist[purchase_url]": str,

    "playlist[release]": str,

    "playlist[release_date]": str,

    "playlist[set_type]": str,

    "playlist[tag_list]": str,
    }, total=False)

class CreateUpdatePlaylistFormRequest(RequiredCreateUpdatePlaylistFormRequest, OptionalCreateUpdatePlaylistFormRequest):
    pass
