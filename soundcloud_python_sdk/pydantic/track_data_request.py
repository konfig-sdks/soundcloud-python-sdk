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


class TrackDataRequest(BaseModel):
    track[title]_: typing.Optional[str] = Field(None, alias='track[title]')

    track[asset_data]_: typing.Optional[typing.IO] = Field(None, alias='track[asset_data]')

    track[permalink]_: typing.Optional[str] = Field(None, alias='track[permalink]')

    track[sharing]_: typing.Optional[Literal["public", "private"]] = Field(None, alias='track[sharing]')

    # who can embed this track \"all\", \"me\", or \"none\"
    track[embeddable_by]_: typing.Optional[Literal["all", "me", "none"]] = Field(None, alias='track[embeddable_by]')

    track[purchase_url]_: typing.Optional[str] = Field(None, alias='track[purchase_url]')

    track[description]_: typing.Optional[str] = Field(None, alias='track[description]')

    track[genre]_: typing.Optional[str] = Field(None, alias='track[genre]')

    # The tag_list property contains a list of tags separated by spaces. Multiword tags are quoted in double quotes. We also support machine tags that follow the pattern NAMESPACE:KEY=VALUE. For example: geo:lat=43.555 camel:size=medium “machine:tag=with space” Machine tags are not revealed to the user on the track pages.
    track[tag_list]_: typing.Optional[str] = Field(None, alias='track[tag_list]')

    track[label_name]_: typing.Optional[str] = Field(None, alias='track[label_name]')

    track[release]_: typing.Optional[str] = Field(None, alias='track[release]')

    # string, formatted as yyyy-mm-dd, representing release date
    track[release_date]_: typing.Optional[str] = Field(None, alias='track[release_date]')

    track[streamable]_: typing.Optional[bool] = Field(None, alias='track[streamable]')

    track[downloadable]_: typing.Optional[bool] = Field(None, alias='track[downloadable]')

    # Possible values: no-rights-reserved, all-rights-reserved, cc-by, cc-by-nc, cc-by-nd, cc-by-sa, cc-by-nc-nd, cc-by-nc-sa
    track[license]_: typing.Optional[Literal["no-rights-reserved", "all-rights-reserved", "cc-by", "cc-by-nc", "cc-by-nd", "cc-by-sa", "cc-by-nc-nd", "cc-by-nc-sa"]] = Field(None, alias='track[license]')

    track[commentable]_: typing.Optional[bool] = Field(None, alias='track[commentable]')

    track[isrc]_: typing.Optional[str] = Field(None, alias='track[isrc]')

    track[artwork_data]_: typing.Optional[typing.IO] = Field(None, alias='track[artwork_data]')
    class Config:
        arbitrary_types_allowed = True
