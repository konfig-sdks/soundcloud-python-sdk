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

from soundcloud_python_sdk.pydantic.me_quota import MeQuota

class Me(BaseModel):
    # description.
    description: typing.Optional[str] = Field(None, alias='description')

    # URL to a JPEG image.
    avatar_url: typing.Optional[str] = Field(None, alias='avatar_url')

    # city.
    city: typing.Optional[str] = Field(None, alias='city')

    # comments count. From now on, the field always has a `0` value.
    comments_count: typing.Optional[int] = Field(None, alias='comments_count')

    # country.
    country: typing.Optional[str] = Field(None, alias='country')

    # created at date
    created_at: typing.Optional[str] = Field(None, alias='created_at')

    # discogs name.
    discogs_name: typing.Optional[str] = Field(None, alias='discogs_name')

    # first name.
    first_name: typing.Optional[str] = Field(None, alias='first_name')

    # number of followers.
    followers_count: typing.Optional[int] = Field(None, alias='followers_count')

    # number of followed users.
    followings_count: typing.Optional[int] = Field(None, alias='followings_count')

    # first and last name.
    full_name: typing.Optional[str] = Field(None, alias='full_name')

    # unique identifier
    id: typing.Optional[int] = Field(None, alias='id')

    # kind of resource.
    kind: typing.Optional[str] = Field(None, alias='kind')

    # last modified timestamp.
    last_modified: typing.Optional[str] = Field(None, alias='last_modified')

    # last name.
    last_name: typing.Optional[str] = Field(None, alias='last_name')

    # likes count.
    likes_count: typing.Optional[int] = Field(None, alias='likes_count')

    # locale.
    locale: typing.Optional[typing.Optional[str]] = Field(None, alias='locale')

    # online.
    online: typing.Optional[bool] = Field(None, alias='online')

    # myspace name
    myspace_name: typing.Optional[str] = Field(None, alias='myspace_name')

    # permalink of the resource.
    permalink: typing.Optional[str] = Field(None, alias='permalink')

    # URL to the SoundCloud.com page.
    permalink_url: typing.Optional[str] = Field(None, alias='permalink_url')

    # subscription plan of the user.
    plan: typing.Optional[str] = Field(None, alias='plan')

    # number of public playlists.
    playlist_count: typing.Optional[int] = Field(None, alias='playlist_count')

    # boolean if email is confirmed.
    primary_email_confirmed: typing.Optional[bool] = Field(None, alias='primary_email_confirmed')

    # number of private playlists.
    private_playlists_count: typing.Optional[int] = Field(None, alias='private_playlists_count')

    # number of private tracks.
    private_tracks_count: typing.Optional[int] = Field(None, alias='private_tracks_count')

    # number of favorited public tracks
    public_favorites_count: typing.Optional[int] = Field(None, alias='public_favorites_count')

    quota: typing.Optional[MeQuota] = Field(None, alias='quota')

    # number of reposts from user
    reposts_count: typing.Optional[int] = Field(None, alias='reposts_count')

    # a list subscriptions associated with the user
    subscriptions: typing.Optional[typing.List[typing.Union[typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]]]] = Field(None, alias='subscriptions')

    # number of public tracks.
    track_count: typing.Optional[int] = Field(None, alias='track_count')

    # upload seconds left.
    upload_seconds_left: typing.Optional[typing.Optional[int]] = Field(None, alias='upload_seconds_left')

    # API resource URL.
    uri: typing.Optional[str] = Field(None, alias='uri')

    # username
    username: typing.Optional[str] = Field(None, alias='username')

    # a URL to the website.
    website: typing.Optional[str] = Field(None, alias='website')

    # a custom title for the website.
    website_title: typing.Optional[str] = Field(None, alias='website_title')
    class Config:
        arbitrary_types_allowed = True
