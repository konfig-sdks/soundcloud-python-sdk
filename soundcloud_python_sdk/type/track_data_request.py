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


RequiredTrackDataRequest = TypedDict("RequiredTrackDataRequest", {
    })

OptionalTrackDataRequest = TypedDict("OptionalTrackDataRequest", {
    "track[title]": str,

    "track[asset_data]": typing.IO,

    "track[permalink]": str,

    "track[sharing]": str,

    # who can embed this track \"all\", \"me\", or \"none\"
    "track[embeddable_by]": str,

    "track[purchase_url]": str,

    "track[description]": str,

    "track[genre]": str,

    # The tag_list property contains a list of tags separated by spaces. Multiword tags are quoted in double quotes. We also support machine tags that follow the pattern NAMESPACE:KEY=VALUE. For example: geo:lat=43.555 camel:size=medium “machine:tag=with space” Machine tags are not revealed to the user on the track pages.
    "track[tag_list]": str,

    "track[label_name]": str,

    "track[release]": str,

    # string, formatted as yyyy-mm-dd, representing release date
    "track[release_date]": str,

    "track[streamable]": bool,

    "track[downloadable]": bool,

    # Possible values: no-rights-reserved, all-rights-reserved, cc-by, cc-by-nc, cc-by-nd, cc-by-sa, cc-by-nc-nd, cc-by-nc-sa
    "track[license]": str,

    "track[commentable]": bool,

    "track[isrc]": str,

    "track[artwork_data]": typing.IO,
    }, total=False)

class TrackDataRequest(RequiredTrackDataRequest, OptionalTrackDataRequest):
    pass
