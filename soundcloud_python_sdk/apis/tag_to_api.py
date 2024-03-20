import typing_extensions

from soundcloud_python_sdk.apis.tags import TagValues
from soundcloud_python_sdk.apis.tags.me_api import MeApi
from soundcloud_python_sdk.apis.tags.tracks_api import TracksApi
from soundcloud_python_sdk.apis.tags.users_api import UsersApi
from soundcloud_python_sdk.apis.tags.playlists_api import PlaylistsApi
from soundcloud_python_sdk.apis.tags.likes_api import LikesApi
from soundcloud_python_sdk.apis.tags.reposts_api import RepostsApi
from soundcloud_python_sdk.apis.tags.search_api import SearchApi
from soundcloud_python_sdk.apis.tags.oauth_api import OauthApi
from soundcloud_python_sdk.apis.tags.miscellaneous_api import MiscellaneousApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ME: MeApi,
        TagValues.TRACKS: TracksApi,
        TagValues.USERS: UsersApi,
        TagValues.PLAYLISTS: PlaylistsApi,
        TagValues.LIKES: LikesApi,
        TagValues.REPOSTS: RepostsApi,
        TagValues.SEARCH: SearchApi,
        TagValues.OAUTH: OauthApi,
        TagValues.MISCELLANEOUS: MiscellaneousApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ME: MeApi,
        TagValues.TRACKS: TracksApi,
        TagValues.USERS: UsersApi,
        TagValues.PLAYLISTS: PlaylistsApi,
        TagValues.LIKES: LikesApi,
        TagValues.REPOSTS: RepostsApi,
        TagValues.SEARCH: SearchApi,
        TagValues.OAUTH: OauthApi,
        TagValues.MISCELLANEOUS: MiscellaneousApi,
    }
)
