# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from soundcloud_python_sdk.paths.me_likes_tracks import Api

from soundcloud_python_sdk.paths import PathValues

path = PathValues.ME_LIKES_TRACKS