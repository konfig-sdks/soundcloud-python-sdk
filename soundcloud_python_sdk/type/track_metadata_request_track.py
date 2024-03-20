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


class RequiredTrackMetadataRequestTrack(TypedDict):
    pass

class OptionalTrackMetadataRequestTrack(TypedDict, total=False):
    title: str

    description: str

    permalink: str

    sharing: str

    # who can embed this track \"all\", \"me\", or \"none\"
    embeddable_by: str

    purchase_url: str

    genre: str

    # The tag_list property contains a list of tags separated by spaces. Multiword tags are quoted in double quotes. We also support machine tags that follow the pattern NAMESPACE:KEY=VALUE. For example: geo:lat=43.555 camel:size=medium “machine:tag=with space” Machine tags are not revealed to the user on the track pages.
    tag_list: str

    label_name: str

    release: str

    # string, formatted as yyyy-mm-dd, representing release date
    release_date: str

    streamable: bool

    downloadable: bool

    # Possible values: no-rights-reserved, all-rights-reserved, cc-by, cc-by-nc, cc-by-nd, cc-by-sa, cc-by-nc-nd, cc-by-nc-sa
    license: str

    commentable: bool

    isrc: str

class TrackMetadataRequestTrack(RequiredTrackMetadataRequestTrack, OptionalTrackMetadataRequestTrack):
    pass
