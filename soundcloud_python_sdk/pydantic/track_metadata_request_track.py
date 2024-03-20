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


class TrackMetadataRequestTrack(BaseModel):
    title: typing.Optional[str] = Field(None, alias='title')

    description: typing.Optional[str] = Field(None, alias='description')

    permalink: typing.Optional[str] = Field(None, alias='permalink')

    sharing: typing.Optional[Literal["public", "private"]] = Field(None, alias='sharing')

    # who can embed this track \"all\", \"me\", or \"none\"
    embeddable_by: typing.Optional[Literal["all", "me", "none"]] = Field(None, alias='embeddable_by')

    purchase_url: typing.Optional[str] = Field(None, alias='purchase_url')

    genre: typing.Optional[str] = Field(None, alias='genre')

    # The tag_list property contains a list of tags separated by spaces. Multiword tags are quoted in double quotes. We also support machine tags that follow the pattern NAMESPACE:KEY=VALUE. For example: geo:lat=43.555 camel:size=medium “machine:tag=with space” Machine tags are not revealed to the user on the track pages.
    tag_list: typing.Optional[str] = Field(None, alias='tag_list')

    label_name: typing.Optional[str] = Field(None, alias='label_name')

    release: typing.Optional[str] = Field(None, alias='release')

    # string, formatted as yyyy-mm-dd, representing release date
    release_date: typing.Optional[str] = Field(None, alias='release_date')

    streamable: typing.Optional[bool] = Field(None, alias='streamable')

    downloadable: typing.Optional[bool] = Field(None, alias='downloadable')

    # Possible values: no-rights-reserved, all-rights-reserved, cc-by, cc-by-nc, cc-by-nd, cc-by-sa, cc-by-nc-nd, cc-by-nc-sa
    license: typing.Optional[Literal["no-rights-reserved", "all-rights-reserved", "cc-by", "cc-by-nc", "cc-by-nd", "cc-by-sa", "cc-by-nc-nd", "cc-by-nc-sa"]] = Field(None, alias='license')

    commentable: typing.Optional[bool] = Field(None, alias='commentable')

    isrc: typing.Optional[str] = Field(None, alias='isrc')
    class Config:
        arbitrary_types_allowed = True
