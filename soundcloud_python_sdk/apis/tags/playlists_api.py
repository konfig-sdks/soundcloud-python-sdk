# coding: utf-8

"""
    SoundCloud Public API Specification

    Discover and play over 320 million music tracks. Join the world’s largest online community of artists, bands, DJs, and audio creators.

    The version of the OpenAPI document: 1.0.0
    Created by: https://github.com/soundcloud/api
"""

from soundcloud_python_sdk.paths.playlists.post import CreateNewPlaylist
from soundcloud_python_sdk.paths.playlists_playlist_id.delete import DeletePlaylist
from soundcloud_python_sdk.paths.playlists_playlist_id.get import GetPlaylistById
from soundcloud_python_sdk.paths.playlists_playlist_id_tracks.get import GetTracks
from soundcloud_python_sdk.paths.playlists_playlist_id_reposters.get import ListReposters
from soundcloud_python_sdk.paths.playlists_playlist_id.put import UpdatePlaylistById
from soundcloud_python_sdk.apis.tags.playlists_api_raw import PlaylistsApiRaw


class PlaylistsApi(
    CreateNewPlaylist,
    DeletePlaylist,
    GetPlaylistById,
    GetTracks,
    ListReposters,
    UpdatePlaylistById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PlaylistsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PlaylistsApiRaw(api_client)
