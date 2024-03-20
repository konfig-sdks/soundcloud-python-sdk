# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from soundcloud_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ME = "me"
    TRACKS = "tracks"
    USERS = "users"
    PLAYLISTS = "playlists"
    LIKES = "likes"
    REPOSTS = "reposts"
    SEARCH = "search"
    OAUTH = "oauth"
    MISCELLANEOUS = "miscellaneous"
