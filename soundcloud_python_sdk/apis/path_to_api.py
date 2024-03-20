import typing_extensions

from soundcloud_python_sdk.paths import PathValues
from soundcloud_python_sdk.apis.paths.connect import Connect
from soundcloud_python_sdk.apis.paths.oauth2_token import Oauth2Token
from soundcloud_python_sdk.apis.paths.me import Me
from soundcloud_python_sdk.apis.paths.me_activities import MeActivities
from soundcloud_python_sdk.apis.paths.me_activities_all_own import MeActivitiesAllOwn
from soundcloud_python_sdk.apis.paths.me_activities_tracks import MeActivitiesTracks
from soundcloud_python_sdk.apis.paths.me_likes_tracks import MeLikesTracks
from soundcloud_python_sdk.apis.paths.me_likes_playlists import MeLikesPlaylists
from soundcloud_python_sdk.apis.paths.me_followings import MeFollowings
from soundcloud_python_sdk.apis.paths.me_followings_tracks import MeFollowingsTracks
from soundcloud_python_sdk.apis.paths.me_followings_user_id import MeFollowingsUserId
from soundcloud_python_sdk.apis.paths.me_followers import MeFollowers
from soundcloud_python_sdk.apis.paths.me_followers_follower_id import MeFollowersFollowerId
from soundcloud_python_sdk.apis.paths.me_playlists import MePlaylists
from soundcloud_python_sdk.apis.paths.me_tracks import MeTracks
from soundcloud_python_sdk.apis.paths.tracks import Tracks
from soundcloud_python_sdk.apis.paths.playlists import Playlists
from soundcloud_python_sdk.apis.paths.users import Users
from soundcloud_python_sdk.apis.paths.playlists_playlist_id import PlaylistsPlaylistId
from soundcloud_python_sdk.apis.paths.playlists_playlist_id_tracks import PlaylistsPlaylistIdTracks
from soundcloud_python_sdk.apis.paths.playlists_playlist_id_reposters import PlaylistsPlaylistIdReposters
from soundcloud_python_sdk.apis.paths.tracks_track_id import TracksTrackId
from soundcloud_python_sdk.apis.paths.tracks_track_id_streams import TracksTrackIdStreams
from soundcloud_python_sdk.apis.paths.tracks_track_id_comments import TracksTrackIdComments
from soundcloud_python_sdk.apis.paths.tracks_track_id_favoriters import TracksTrackIdFavoriters
from soundcloud_python_sdk.apis.paths.tracks_track_id_reposters import TracksTrackIdReposters
from soundcloud_python_sdk.apis.paths.tracks_track_id_related import TracksTrackIdRelated
from soundcloud_python_sdk.apis.paths.resolve import Resolve
from soundcloud_python_sdk.apis.paths.users_user_id import UsersUserId
from soundcloud_python_sdk.apis.paths.users_user_id_favorites import UsersUserIdFavorites
from soundcloud_python_sdk.apis.paths.users_user_id_followers import UsersUserIdFollowers
from soundcloud_python_sdk.apis.paths.users_user_id_followings import UsersUserIdFollowings
from soundcloud_python_sdk.apis.paths.users_user_id_followings_following_id import UsersUserIdFollowingsFollowingId
from soundcloud_python_sdk.apis.paths.users_user_id_playlists import UsersUserIdPlaylists
from soundcloud_python_sdk.apis.paths.users_user_id_tracks import UsersUserIdTracks
from soundcloud_python_sdk.apis.paths.users_user_id_web_profiles import UsersUserIdWebProfiles
from soundcloud_python_sdk.apis.paths.users_user_id_likes_tracks import UsersUserIdLikesTracks
from soundcloud_python_sdk.apis.paths.users_user_id_likes_playlists import UsersUserIdLikesPlaylists
from soundcloud_python_sdk.apis.paths.likes_tracks_track_id import LikesTracksTrackId
from soundcloud_python_sdk.apis.paths.likes_playlists_playlist_id import LikesPlaylistsPlaylistId
from soundcloud_python_sdk.apis.paths.reposts_tracks_track_id import RepostsTracksTrackId
from soundcloud_python_sdk.apis.paths.reposts_playlists_playlist_id import RepostsPlaylistsPlaylistId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.CONNECT: Connect,
        PathValues.OAUTH2_TOKEN: Oauth2Token,
        PathValues.ME: Me,
        PathValues.ME_ACTIVITIES: MeActivities,
        PathValues.ME_ACTIVITIES_ALL_OWN: MeActivitiesAllOwn,
        PathValues.ME_ACTIVITIES_TRACKS: MeActivitiesTracks,
        PathValues.ME_LIKES_TRACKS: MeLikesTracks,
        PathValues.ME_LIKES_PLAYLISTS: MeLikesPlaylists,
        PathValues.ME_FOLLOWINGS: MeFollowings,
        PathValues.ME_FOLLOWINGS_TRACKS: MeFollowingsTracks,
        PathValues.ME_FOLLOWINGS_USER_ID: MeFollowingsUserId,
        PathValues.ME_FOLLOWERS: MeFollowers,
        PathValues.ME_FOLLOWERS_FOLLOWER_ID: MeFollowersFollowerId,
        PathValues.ME_PLAYLISTS: MePlaylists,
        PathValues.ME_TRACKS: MeTracks,
        PathValues.TRACKS: Tracks,
        PathValues.PLAYLISTS: Playlists,
        PathValues.USERS: Users,
        PathValues.PLAYLISTS_PLAYLIST_ID: PlaylistsPlaylistId,
        PathValues.PLAYLISTS_PLAYLIST_ID_TRACKS: PlaylistsPlaylistIdTracks,
        PathValues.PLAYLISTS_PLAYLIST_ID_REPOSTERS: PlaylistsPlaylistIdReposters,
        PathValues.TRACKS_TRACK_ID: TracksTrackId,
        PathValues.TRACKS_TRACK_ID_STREAMS: TracksTrackIdStreams,
        PathValues.TRACKS_TRACK_ID_COMMENTS: TracksTrackIdComments,
        PathValues.TRACKS_TRACK_ID_FAVORITERS: TracksTrackIdFavoriters,
        PathValues.TRACKS_TRACK_ID_REPOSTERS: TracksTrackIdReposters,
        PathValues.TRACKS_TRACK_ID_RELATED: TracksTrackIdRelated,
        PathValues.RESOLVE: Resolve,
        PathValues.USERS_USER_ID: UsersUserId,
        PathValues.USERS_USER_ID_FAVORITES: UsersUserIdFavorites,
        PathValues.USERS_USER_ID_FOLLOWERS: UsersUserIdFollowers,
        PathValues.USERS_USER_ID_FOLLOWINGS: UsersUserIdFollowings,
        PathValues.USERS_USER_ID_FOLLOWINGS_FOLLOWING_ID: UsersUserIdFollowingsFollowingId,
        PathValues.USERS_USER_ID_PLAYLISTS: UsersUserIdPlaylists,
        PathValues.USERS_USER_ID_TRACKS: UsersUserIdTracks,
        PathValues.USERS_USER_ID_WEBPROFILES: UsersUserIdWebProfiles,
        PathValues.USERS_USER_ID_LIKES_TRACKS: UsersUserIdLikesTracks,
        PathValues.USERS_USER_ID_LIKES_PLAYLISTS: UsersUserIdLikesPlaylists,
        PathValues.LIKES_TRACKS_TRACK_ID: LikesTracksTrackId,
        PathValues.LIKES_PLAYLISTS_PLAYLIST_ID: LikesPlaylistsPlaylistId,
        PathValues.REPOSTS_TRACKS_TRACK_ID: RepostsTracksTrackId,
        PathValues.REPOSTS_PLAYLISTS_PLAYLIST_ID: RepostsPlaylistsPlaylistId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.CONNECT: Connect,
        PathValues.OAUTH2_TOKEN: Oauth2Token,
        PathValues.ME: Me,
        PathValues.ME_ACTIVITIES: MeActivities,
        PathValues.ME_ACTIVITIES_ALL_OWN: MeActivitiesAllOwn,
        PathValues.ME_ACTIVITIES_TRACKS: MeActivitiesTracks,
        PathValues.ME_LIKES_TRACKS: MeLikesTracks,
        PathValues.ME_LIKES_PLAYLISTS: MeLikesPlaylists,
        PathValues.ME_FOLLOWINGS: MeFollowings,
        PathValues.ME_FOLLOWINGS_TRACKS: MeFollowingsTracks,
        PathValues.ME_FOLLOWINGS_USER_ID: MeFollowingsUserId,
        PathValues.ME_FOLLOWERS: MeFollowers,
        PathValues.ME_FOLLOWERS_FOLLOWER_ID: MeFollowersFollowerId,
        PathValues.ME_PLAYLISTS: MePlaylists,
        PathValues.ME_TRACKS: MeTracks,
        PathValues.TRACKS: Tracks,
        PathValues.PLAYLISTS: Playlists,
        PathValues.USERS: Users,
        PathValues.PLAYLISTS_PLAYLIST_ID: PlaylistsPlaylistId,
        PathValues.PLAYLISTS_PLAYLIST_ID_TRACKS: PlaylistsPlaylistIdTracks,
        PathValues.PLAYLISTS_PLAYLIST_ID_REPOSTERS: PlaylistsPlaylistIdReposters,
        PathValues.TRACKS_TRACK_ID: TracksTrackId,
        PathValues.TRACKS_TRACK_ID_STREAMS: TracksTrackIdStreams,
        PathValues.TRACKS_TRACK_ID_COMMENTS: TracksTrackIdComments,
        PathValues.TRACKS_TRACK_ID_FAVORITERS: TracksTrackIdFavoriters,
        PathValues.TRACKS_TRACK_ID_REPOSTERS: TracksTrackIdReposters,
        PathValues.TRACKS_TRACK_ID_RELATED: TracksTrackIdRelated,
        PathValues.RESOLVE: Resolve,
        PathValues.USERS_USER_ID: UsersUserId,
        PathValues.USERS_USER_ID_FAVORITES: UsersUserIdFavorites,
        PathValues.USERS_USER_ID_FOLLOWERS: UsersUserIdFollowers,
        PathValues.USERS_USER_ID_FOLLOWINGS: UsersUserIdFollowings,
        PathValues.USERS_USER_ID_FOLLOWINGS_FOLLOWING_ID: UsersUserIdFollowingsFollowingId,
        PathValues.USERS_USER_ID_PLAYLISTS: UsersUserIdPlaylists,
        PathValues.USERS_USER_ID_TRACKS: UsersUserIdTracks,
        PathValues.USERS_USER_ID_WEBPROFILES: UsersUserIdWebProfiles,
        PathValues.USERS_USER_ID_LIKES_TRACKS: UsersUserIdLikesTracks,
        PathValues.USERS_USER_ID_LIKES_PLAYLISTS: UsersUserIdLikesPlaylists,
        PathValues.LIKES_TRACKS_TRACK_ID: LikesTracksTrackId,
        PathValues.LIKES_PLAYLISTS_PLAYLIST_ID: LikesPlaylistsPlaylistId,
        PathValues.REPOSTS_TRACKS_TRACK_ID: RepostsTracksTrackId,
        PathValues.REPOSTS_PLAYLISTS_PLAYLIST_ID: RepostsPlaylistsPlaylistId,
    }
)
