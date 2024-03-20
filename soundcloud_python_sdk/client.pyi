# coding: utf-8
"""
    SoundCloud Public API Specification

    Discover and play over 320 million music tracks. Join the world’s largest online community of artists, bands, DJs, and audio creators.

    The version of the OpenAPI document: 1.0.0
    Created by: https://github.com/soundcloud/api
"""

import typing
import inspect
from datetime import date, datetime
from soundcloud_python_sdk.client_custom import ClientCustom
from soundcloud_python_sdk.configuration import Configuration
from soundcloud_python_sdk.api_client import ApiClient
from soundcloud_python_sdk.type_util import copy_signature
from soundcloud_python_sdk.apis.tags.likes_api import LikesApi
from soundcloud_python_sdk.apis.tags.me_api import MeApi
from soundcloud_python_sdk.apis.tags.miscellaneous_api import MiscellaneousApi
from soundcloud_python_sdk.apis.tags.oauth_api import OauthApi
from soundcloud_python_sdk.apis.tags.playlists_api import PlaylistsApi
from soundcloud_python_sdk.apis.tags.reposts_api import RepostsApi
from soundcloud_python_sdk.apis.tags.search_api import SearchApi
from soundcloud_python_sdk.apis.tags.tracks_api import TracksApi
from soundcloud_python_sdk.apis.tags.users_api import UsersApi



class SoundCloud(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.likes: LikesApi = LikesApi(api_client)
        self.me: MeApi = MeApi(api_client)
        self.miscellaneous: MiscellaneousApi = MiscellaneousApi(api_client)
        self.oauth: OauthApi = OauthApi(api_client)
        self.playlists: PlaylistsApi = PlaylistsApi(api_client)
        self.reposts: RepostsApi = RepostsApi(api_client)
        self.search: SearchApi = SearchApi(api_client)
        self.tracks: TracksApi = TracksApi(api_client)
        self.users: UsersApi = UsersApi(api_client)
