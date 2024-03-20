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


class RequiredUser(TypedDict):
    pass

class OptionalUser(TypedDict, total=False):
    # description
    description: str

    # URL to a JPEG image
    avatar_url: str

    # city
    city: str

    # country
    country: str

    # discogs name
    discogs_name: str

    # first name
    first_name: str

    # number of followers
    followers_count: int

    # number of followed users
    followings_count: int

    # first and last name
    full_name: str

    # unique identifier
    id: int

    # kind of resource
    kind: str

    # profile creation datetime
    created_at: datetime

    # last modified datetime
    last_modified: datetime

    # last name
    last_name: str

    # myspace name
    myspace_name: str

    # permalink of the resource
    permalink: str

    # URL to the SoundCloud.com page
    permalink_url: str

    # subscription plan of the user
    plan: str

    # number of public playlists
    playlist_count: int

    # number of favorited public tracks
    public_favorites_count: int

    # number of reposts from user
    reposts_count: int

    # number of public tracks
    track_count: int

    # API resource URL
    uri: str

    # username
    username: str

    # a URL to the website
    website: str

    # a custom title for the website
    website_title: str

    # a list subscriptions associated with the user
    subscriptions: typing.List[typing.Union[typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]]]

class User(RequiredUser, OptionalUser):
    pass
