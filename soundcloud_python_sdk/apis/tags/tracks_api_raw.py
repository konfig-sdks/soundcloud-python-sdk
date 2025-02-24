# coding: utf-8

"""
    SoundCloud Public API Specification

    Discover and play over 320 million music tracks. Join the world’s largest online community of artists, bands, DJs, and audio creators.

    The version of the OpenAPI document: 1.0.0
    Created by: https://github.com/soundcloud/api
"""

from soundcloud_python_sdk.paths.tracks_track_id_comments.post import CreateCommentRaw
from soundcloud_python_sdk.paths.tracks_track_id.delete import DeleteTrackRaw
from soundcloud_python_sdk.paths.tracks_track_id.get import GetByIdRaw
from soundcloud_python_sdk.paths.tracks_track_id_comments.get import GetCommentsRaw
from soundcloud_python_sdk.paths.tracks_track_id_favoriters.get import GetFavoritersRaw
from soundcloud_python_sdk.paths.tracks_track_id_related.get import GetRelatedTracksRaw
from soundcloud_python_sdk.paths.tracks_track_id_streams.get import GetStreamableUrlsRaw
from soundcloud_python_sdk.paths.tracks_track_id_reposters.get import ListRepostersRaw
from soundcloud_python_sdk.paths.tracks_track_id.put import UpdateTrackInformationRaw
from soundcloud_python_sdk.paths.tracks.post import UploadNewTrackRaw


class TracksApiRaw(
    CreateCommentRaw,
    DeleteTrackRaw,
    GetByIdRaw,
    GetCommentsRaw,
    GetFavoritersRaw,
    GetRelatedTracksRaw,
    GetStreamableUrlsRaw,
    ListRepostersRaw,
    UpdateTrackInformationRaw,
    UploadNewTrackRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
