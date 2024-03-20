operation_parameter_map = {
    '/likes/playlists/{playlist_id}-POST': {
        'parameters': [
            {
                'name': 'playlist_id'
            },
        ]
    },
    '/likes/tracks/{track_id}-POST': {
        'parameters': [
            {
                'name': 'track_id'
            },
        ]
    },
    '/likes/playlists/{playlist_id}-DELETE': {
        'parameters': [
            {
                'name': 'playlist_id'
            },
        ]
    },
    '/likes/tracks/{track_id}-DELETE': {
        'parameters': [
            {
                'name': 'track_id'
            },
        ]
    },
    '/me/followings/{user_id}-DELETE': {
        'parameters': [
            {
                'name': 'user_id'
            },
        ]
    },
    '/me/followings/{user_id}-PUT': {
        'parameters': [
            {
                'name': 'user_id'
            },
        ]
    },
    '/me/activities-GET': {
        'parameters': [
            {
                'name': 'access'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/me/followings/{user_id}-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
        ]
    },
    '/me/followings-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/me/followers/{follower_id}-GET': {
        'parameters': [
            {
                'name': 'follower_id'
            },
        ]
    },
    '/me/followers-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
        ]
    },
    '/me/likes/playlists-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'linked_partitioning'
            },
        ]
    },
    '/me/activities/all/own-GET': {
        'parameters': [
            {
                'name': 'access'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/me/activities/tracks-GET': {
        'parameters': [
            {
                'name': 'access'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/me-GET': {
        'parameters': [
        ]
    },
    '/me/followings/tracks-GET': {
        'parameters': [
            {
                'name': 'access'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/me/likes/tracks-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'access'
            },
            {
                'name': 'linked_partitioning'
            },
        ]
    },
    '/me/playlists-GET': {
        'parameters': [
            {
                'name': 'show_tracks'
            },
            {
                'name': 'linked_partitioning'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/me/tracks-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'linked_partitioning'
            },
        ]
    },
    '/resolve-GET': {
        'parameters': [
            {
                'name': 'url'
            },
        ]
    },
    '/connect-GET': {
        'parameters': [
            {
                'name': 'client_id'
            },
            {
                'name': 'redirect_uri'
            },
            {
                'name': 'response_type'
            },
            {
                'name': 'state'
            },
        ]
    },
    '/oauth2/token-POST': {
        'parameters': [
            {
                'name': 'grant_type'
            },
            {
                'name': 'client_id'
            },
            {
                'name': 'client_secret'
            },
            {
                'name': 'code'
            },
            {
                'name': 'redirect_uri'
            },
            {
                'name': 'refresh_token'
            },
        ]
    },
    '/playlists-POST': {
        'parameters': [
            {
                'name': 'playlist'
            },
        ]
    },
    '/playlists/{playlist_id}-DELETE': {
        'parameters': [
            {
                'name': 'playlist_id'
            },
        ]
    },
    '/playlists/{playlist_id}-GET': {
        'parameters': [
            {
                'name': 'playlist_id'
            },
            {
                'name': 'secret_token'
            },
            {
                'name': 'access'
            },
            {
                'name': 'show_tracks'
            },
        ]
    },
    '/playlists/{playlist_id}/tracks-GET': {
        'parameters': [
            {
                'name': 'playlist_id'
            },
            {
                'name': 'secret_token'
            },
            {
                'name': 'access'
            },
            {
                'name': 'linked_partitioning'
            },
        ]
    },
    '/playlists/{playlist_id}/reposters-GET': {
        'parameters': [
            {
                'name': 'playlist_id'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/playlists/{playlist_id}-PUT': {
        'parameters': [
            {
                'name': 'playlist_id'
            },
            {
                'name': 'playlist'
            },
        ]
    },
    '/reposts/playlists/{playlist_id}-POST': {
        'parameters': [
            {
                'name': 'playlist_id'
            },
        ]
    },
    '/reposts/tracks/{track_id}-DELETE': {
        'parameters': [
            {
                'name': 'track_id'
            },
        ]
    },
    '/reposts/playlists/{playlist_id}-DELETE': {
        'parameters': [
            {
                'name': 'playlist_id'
            },
        ]
    },
    '/reposts/tracks/{track_id}-POST': {
        'parameters': [
            {
                'name': 'track_id'
            },
        ]
    },
    '/tracks-GET': {
        'parameters': [
            {
                'name': 'q'
            },
            {
                'name': 'ids'
            },
            {
                'name': 'genres'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'bpm'
            },
            {
                'name': 'duration'
            },
            {
                'name': 'created_at'
            },
            {
                'name': 'access'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'linked_partitioning'
            },
        ]
    },
    '/playlists-GET': {
        'parameters': [
            {
                'name': 'q'
            },
            {
                'name': 'access'
            },
            {
                'name': 'show_tracks'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'linked_partitioning'
            },
        ]
    },
    '/users-GET': {
        'parameters': [
            {
                'name': 'q'
            },
            {
                'name': 'ids'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'linked_partitioning'
            },
        ]
    },
    '/tracks/{track_id}/comments-POST': {
        'parameters': [
            {
                'name': 'track_id'
            },
            {
                'name': 'comment'
            },
        ]
    },
    '/tracks/{track_id}-DELETE': {
        'parameters': [
            {
                'name': 'track_id'
            },
        ]
    },
    '/tracks/{track_id}-GET': {
        'parameters': [
            {
                'name': 'track_id'
            },
            {
                'name': 'secret_token'
            },
        ]
    },
    '/tracks/{track_id}/comments-GET': {
        'parameters': [
            {
                'name': 'track_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'linked_partitioning'
            },
        ]
    },
    '/tracks/{track_id}/favoriters-GET': {
        'parameters': [
            {
                'name': 'track_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'linked_partitioning'
            },
        ]
    },
    '/tracks/{track_id}/related-GET': {
        'parameters': [
            {
                'name': 'track_id'
            },
            {
                'name': 'access'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'linked_partitioning'
            },
        ]
    },
    '/tracks/{track_id}/streams-GET': {
        'parameters': [
            {
                'name': 'track_id'
            },
            {
                'name': 'secret_token'
            },
        ]
    },
    '/tracks/{track_id}/reposters-GET': {
        'parameters': [
            {
                'name': 'track_id'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/tracks/{track_id}-PUT': {
        'parameters': [
            {
                'name': 'track_id'
            },
            {
                'name': 'track'
            },
        ]
    },
    '/tracks-POST': {
        'parameters': [
            {
                'name': 'track[title]'
            },
            {
                'name': 'track[asset_data]'
            },
            {
                'name': 'track[permalink]'
            },
            {
                'name': 'track[sharing]'
            },
            {
                'name': 'track[embeddable_by]'
            },
            {
                'name': 'track[purchase_url]'
            },
            {
                'name': 'track[description]'
            },
            {
                'name': 'track[genre]'
            },
            {
                'name': 'track[tag_list]'
            },
            {
                'name': 'track[label_name]'
            },
            {
                'name': 'track[release]'
            },
            {
                'name': 'track[release_date]'
            },
            {
                'name': 'track[streamable]'
            },
            {
                'name': 'track[downloadable]'
            },
            {
                'name': 'track[license]'
            },
            {
                'name': 'track[commentable]'
            },
            {
                'name': 'track[isrc]'
            },
            {
                'name': 'track[artwork_data]'
            },
        ]
    },
    '/users/{user_id}/followers-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/users/{user_id}/followings/{following_id}-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'following_id'
            },
        ]
    },
    '/users/{user_id}-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/followings-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/users/{user_id}/playlists-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'access'
            },
            {
                'name': 'show_tracks'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'linked_partitioning'
            },
        ]
    },
    '/users/{user_id}/tracks-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'access'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'linked_partitioning'
            },
        ]
    },
    '/users/{user_id}/web-profiles-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/users/{user_id}/favorites-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'linked_partitioning'
            },
        ]
    },
    '/users/{user_id}/likes/playlists-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'linked_partitioning'
            },
        ]
    },
    '/users/{user_id}/likes/tracks-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'access'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'linked_partitioning'
            },
        ]
    },
};