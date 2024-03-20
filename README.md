<div align="left">

[![Visit Soundcloud](./header.png)](https://developers.soundcloud.com)

# Soundcloud<a id="soundcloud"></a>

Discover and play over 320 million music tracks. Join the world’s largest online community of artists, bands, DJs, and audio creators.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`soundcloud.likes.playlist`](#soundcloudlikesplaylist)
  * [`soundcloud.likes.track_action`](#soundcloudlikestrack_action)
  * [`soundcloud.likes.unlike_playlist`](#soundcloudlikesunlike_playlist)
  * [`soundcloud.likes.unlike_track`](#soundcloudlikesunlike_track)
  * [`soundcloud.me.delete_followed_user`](#soundcloudmedelete_followed_user)
  * [`soundcloud.me.follow_user`](#soundcloudmefollow_user)
  * [`soundcloud.me.get_activities`](#soundcloudmeget_activities)
  * [`soundcloud.me.get_followed_user`](#soundcloudmeget_followed_user)
  * [`soundcloud.me.get_followed_users`](#soundcloudmeget_followed_users)
  * [`soundcloud.me.get_follower_by_id`](#soundcloudmeget_follower_by_id)
  * [`soundcloud.me.get_followers_list`](#soundcloudmeget_followers_list)
  * [`soundcloud.me.get_liked_playlists`](#soundcloudmeget_liked_playlists)
  * [`soundcloud.me.get_recent_activities`](#soundcloudmeget_recent_activities)
  * [`soundcloud.me.get_recent_tracks`](#soundcloudmeget_recent_tracks)
  * [`soundcloud.me.get_user_information`](#soundcloudmeget_user_information)
  * [`soundcloud.me.list_followed_tracks`](#soundcloudmelist_followed_tracks)
  * [`soundcloud.me.list_liked_tracks`](#soundcloudmelist_liked_tracks)
  * [`soundcloud.me.list_playlists_info_tracks_owner`](#soundcloudmelist_playlists_info_tracks_owner)
  * [`soundcloud.me.list_user_tracks`](#soundcloudmelist_user_tracks)
  * [`soundcloud.miscellaneous.resolve_soundcloud_urls`](#soundcloudmiscellaneousresolve_soundcloud_urls)
  * [`soundcloud.oauth.authorize_user`](#soundcloudoauthauthorize_user)
  * [`soundcloud.oauth.provision_access_token`](#soundcloudoauthprovision_access_token)
  * [`soundcloud.playlists.create_new_playlist`](#soundcloudplaylistscreate_new_playlist)
  * [`soundcloud.playlists.delete_playlist`](#soundcloudplaylistsdelete_playlist)
  * [`soundcloud.playlists.get_playlist_by_id`](#soundcloudplaylistsget_playlist_by_id)
  * [`soundcloud.playlists.get_tracks`](#soundcloudplaylistsget_tracks)
  * [`soundcloud.playlists.list_reposters`](#soundcloudplaylistslist_reposters)
  * [`soundcloud.playlists.update_playlist_by_id`](#soundcloudplaylistsupdate_playlist_by_id)
  * [`soundcloud.reposts.playlist_as_authenticated_user`](#soundcloudrepostsplaylist_as_authenticated_user)
  * [`soundcloud.reposts.remove_repost`](#soundcloudrepostsremove_repost)
  * [`soundcloud.reposts.remove_repost_on_playlist`](#soundcloudrepostsremove_repost_on_playlist)
  * [`soundcloud.reposts.track_as_authenticated_user`](#soundcloudrepoststrack_as_authenticated_user)
  * [`soundcloud.search.by_query`](#soundcloudsearchby_query)
  * [`soundcloud.search.by_query_0`](#soundcloudsearchby_query_0)
  * [`soundcloud.search.user_query`](#soundcloudsearchuser_query)
  * [`soundcloud.tracks.create_comment`](#soundcloudtrackscreate_comment)
  * [`soundcloud.tracks.delete_track`](#soundcloudtracksdelete_track)
  * [`soundcloud.tracks.get_by_id`](#soundcloudtracksget_by_id)
  * [`soundcloud.tracks.get_comments`](#soundcloudtracksget_comments)
  * [`soundcloud.tracks.get_favoriters`](#soundcloudtracksget_favoriters)
  * [`soundcloud.tracks.get_related_tracks`](#soundcloudtracksget_related_tracks)
  * [`soundcloud.tracks.get_streamable_urls`](#soundcloudtracksget_streamable_urls)
  * [`soundcloud.tracks.list_reposters`](#soundcloudtrackslist_reposters)
  * [`soundcloud.tracks.update_track_information`](#soundcloudtracksupdate_track_information)
  * [`soundcloud.tracks.upload_new_track`](#soundcloudtracksupload_new_track)
  * [`soundcloud.users.get_followers`](#soundcloudusersget_followers)
  * [`soundcloud.users.get_following_by_id`](#soundcloudusersget_following_by_id)
  * [`soundcloud.users.get_user`](#soundcloudusersget_user)
  * [`soundcloud.users.get_user_followings`](#soundcloudusersget_user_followings)
  * [`soundcloud.users.get_user_playlists`](#soundcloudusersget_user_playlists)
  * [`soundcloud.users.get_user_tracks`](#soundcloudusersget_user_tracks)
  * [`soundcloud.users.get_user_web_profiles`](#soundcloudusersget_user_web_profiles)
  * [`soundcloud.users.list_favorites`](#soundclouduserslist_favorites)
  * [`soundcloud.users.list_liked_playlists`](#soundclouduserslist_liked_playlists)
  * [`soundcloud.users.list_liked_tracks`](#soundclouduserslist_liked_tracks)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=SoundCloud&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from soundcloud_python_sdk import SoundCloud, ApiException

soundcloud = SoundCloud(
    auth_header="YOUR_API_KEY",
)

try:
    # Likes a playlist.
    soundcloud.likes.playlist(
        playlist_id=1212781357,
    )
except ApiException as e:
    print("Exception when calling LikesApi.playlist: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["code"])
        pprint(e.body["message"])
        pprint(e.body["link"])
        pprint(e.body["error"])
        pprint(e.body["errors"])
        pprint(e.body["status"])
    if e.status == 401:
        pprint(e.body["code"])
        pprint(e.body["message"])
        pprint(e.body["link"])
        pprint(e.body["error"])
        pprint(e.body["errors"])
        pprint(e.body["status"])
    if e.status == 404:
        pprint(e.body["code"])
        pprint(e.body["message"])
        pprint(e.body["link"])
        pprint(e.body["error"])
        pprint(e.body["errors"])
        pprint(e.body["status"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from soundcloud_python_sdk import SoundCloud, ApiException

soundcloud = SoundCloud(
    auth_header="YOUR_API_KEY",
)


async def main():
    try:
        # Likes a playlist.
        await soundcloud.likes.aplaylist(
            playlist_id=1212781357,
        )
    except ApiException as e:
        print("Exception when calling LikesApi.playlist: %s\n" % e)
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["code"])
            pprint(e.body["message"])
            pprint(e.body["link"])
            pprint(e.body["error"])
            pprint(e.body["errors"])
            pprint(e.body["status"])
        if e.status == 401:
            pprint(e.body["code"])
            pprint(e.body["message"])
            pprint(e.body["link"])
            pprint(e.body["error"])
            pprint(e.body["errors"])
            pprint(e.body["status"])
        if e.status == 404:
            pprint(e.body["code"])
            pprint(e.body["message"])
            pprint(e.body["link"])
            pprint(e.body["error"])
            pprint(e.body["errors"])
            pprint(e.body["status"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from soundcloud_python_sdk import SoundCloud, ApiException

soundcloud = SoundCloud(
    auth_header="YOUR_API_KEY",
)

try:
    # Likes a playlist.
    playlist_response = soundcloud.likes.raw.playlist(
        playlist_id=1212781357,
    )
    pprint(playlist_response.headers)
    pprint(playlist_response.status)
    pprint(playlist_response.round_trip_time)
except ApiException as e:
    print("Exception when calling LikesApi.playlist: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["code"])
        pprint(e.body["message"])
        pprint(e.body["link"])
        pprint(e.body["error"])
        pprint(e.body["errors"])
        pprint(e.body["status"])
    if e.status == 401:
        pprint(e.body["code"])
        pprint(e.body["message"])
        pprint(e.body["link"])
        pprint(e.body["error"])
        pprint(e.body["errors"])
        pprint(e.body["status"])
    if e.status == 404:
        pprint(e.body["code"])
        pprint(e.body["message"])
        pprint(e.body["link"])
        pprint(e.body["error"])
        pprint(e.body["errors"])
        pprint(e.body["status"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `soundcloud.likes.playlist`<a id="soundcloudlikesplaylist"></a>

Likes a playlist.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
soundcloud.likes.playlist(
    playlist_id=1212781357,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `int`<a id="playlist_id-int"></a>

SoundCloud playlist id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/likes/playlists/{playlist_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.likes.track_action`<a id="soundcloudlikestrack_action"></a>

Likes a track.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
soundcloud.likes.track_action(
    track_id=1015448728,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### track_id: `int`<a id="track_id-int"></a>

SoundCloud Track id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/likes/tracks/{track_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.likes.unlike_playlist`<a id="soundcloudlikesunlike_playlist"></a>

Unlikes a playlist.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
soundcloud.likes.unlike_playlist(
    playlist_id=1212781357,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `int`<a id="playlist_id-int"></a>

SoundCloud playlist id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/likes/playlists/{playlist_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.likes.unlike_track`<a id="soundcloudlikesunlike_track"></a>

Unlikes a track.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
soundcloud.likes.unlike_track(
    track_id=1015448728,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### track_id: `int`<a id="track_id-int"></a>

SoundCloud Track id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/likes/tracks/{track_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.me.delete_followed_user`<a id="soundcloudmedelete_followed_user"></a>

Deletes a user who is followed by the authenticated user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
soundcloud.me.delete_followed_user(
    user_id=743372812,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `int`<a id="user_id-int"></a>

SoundCloud User id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/followings/{user_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.me.follow_user`<a id="soundcloudmefollow_user"></a>

Follows a user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
soundcloud.me.follow_user(
    user_id=743372812,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `int`<a id="user_id-int"></a>

SoundCloud User id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/followings/{user_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.me.get_activities`<a id="soundcloudmeget_activities"></a>

Returns the authenticated user's activities.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_activities_response = soundcloud.me.get_activities(
    access=["playable,preview"],
    limit=2,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### access: List[`str`]<a id="access-liststr"></a>

Filters content by level of access the user (logged in or anonymous) has to the track. The result list will include only tracks with the specified access. Include all options if you'd like to see all possible tracks. See `Track#access` schema for more details. 

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

#### 🔄 Return<a id="🔄-return"></a>

[`Activities`](./soundcloud_python_sdk/pydantic/activities.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/activities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.me.get_followed_user`<a id="soundcloudmeget_followed_user"></a>

Returns a user who is followed by the authenticated user. (use /users/{user_id} instead, to fetch the user details)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_followed_user_response = soundcloud.me.get_followed_user(
    user_id=948745750,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `int`<a id="user_id-int"></a>

SoundCloud User id

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./soundcloud_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/followings/{user_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.me.get_followed_users`<a id="soundcloudmeget_followed_users"></a>

Returns a list of users who are followed by the authenticated user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_followed_users_response = soundcloud.me.get_followed_users(
    limit=2,
    offset=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

##### offset: `int`<a id="offset-int"></a>

Offset of first result. Deprecated, use `linked_partitioning` instead.

#### 🔄 Return<a id="🔄-return"></a>

[`Users`](./soundcloud_python_sdk/pydantic/users.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/followings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.me.get_follower_by_id`<a id="soundcloudmeget_follower_by_id"></a>

Returns a user who is following the authenticated user. (use /users/{user_id} instead, to fetch the user details)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_follower_by_id_response = soundcloud.me.get_follower_by_id(
    follower_id=743372812,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### follower_id: `int`<a id="follower_id-int"></a>

SoundCloud User id to denote a Follower

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./soundcloud_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/followers/{follower_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.me.get_followers_list`<a id="soundcloudmeget_followers_list"></a>

Returns a list of users who are following the authenticated user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_followers_list_response = soundcloud.me.get_followers_list(
    limit=2,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

#### 🔄 Return<a id="🔄-return"></a>

[`Users`](./soundcloud_python_sdk/pydantic/users.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/followers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.me.get_liked_playlists`<a id="soundcloudmeget_liked_playlists"></a>

Returns a list of favorited or liked playlists of the authenticated user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_liked_playlists_response = soundcloud.me.get_liked_playlists(
    limit=2,
    linked_partitioning=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

##### linked_partitioning: `bool`<a id="linked_partitioning-bool"></a>

Returns paginated collection of items (recommended, returning a list without pagination is deprecated and should not be used)

#### 🔄 Return<a id="🔄-return"></a>

[`MeGetLikedPlaylistsResponse`](./soundcloud_python_sdk/pydantic/me_get_liked_playlists_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/likes/playlists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.me.get_recent_activities`<a id="soundcloudmeget_recent_activities"></a>

Recent the authenticated user's activities.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_recent_activities_response = soundcloud.me.get_recent_activities(
    access=["playable,preview"],
    limit=2,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### access: List[`str`]<a id="access-liststr"></a>

Filters content by level of access the user (logged in or anonymous) has to the track. The result list will include only tracks with the specified access. Include all options if you'd like to see all possible tracks. See `Track#access` schema for more details. 

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

#### 🔄 Return<a id="🔄-return"></a>

[`Activities`](./soundcloud_python_sdk/pydantic/activities.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/activities/all/own` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.me.get_recent_tracks`<a id="soundcloudmeget_recent_tracks"></a>

Returns the authenticated user's recent track related activities.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_recent_tracks_response = soundcloud.me.get_recent_tracks(
    access=["playable,preview"],
    limit=2,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### access: List[`str`]<a id="access-liststr"></a>

Filters content by level of access the user (logged in or anonymous) has to the track. The result list will include only tracks with the specified access. Include all options if you'd like to see all possible tracks. See `Track#access` schema for more details. 

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

#### 🔄 Return<a id="🔄-return"></a>

[`Activities`](./soundcloud_python_sdk/pydantic/activities.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/activities/tracks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.me.get_user_information`<a id="soundcloudmeget_user_information"></a>

Returns the authenticated user’s information.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_information_response = soundcloud.me.get_user_information()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Me`](./soundcloud_python_sdk/pydantic/me.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.me.list_followed_tracks`<a id="soundcloudmelist_followed_tracks"></a>

Returns a list of recent tracks from users followed by the authenticated user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_followed_tracks_response = soundcloud.me.list_followed_tracks(
    access=["playable,preview"],
    limit=2,
    offset=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### access: List[`str`]<a id="access-liststr"></a>

Filters content by level of access the user (logged in or anonymous) has to the track. The result list will include only tracks with the specified access. Include all options if you'd like to see all possible tracks. See `Track#access` schema for more details. 

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

##### offset: `int`<a id="offset-int"></a>

Offset of first result. Deprecated, use `linked_partitioning` instead.

#### 🔄 Return<a id="🔄-return"></a>

[`TracksList`](./soundcloud_python_sdk/pydantic/tracks_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/followings/tracks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.me.list_liked_tracks`<a id="soundcloudmelist_liked_tracks"></a>

Returns a list of favorited or liked tracks of the authenticated user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_liked_tracks_response = soundcloud.me.list_liked_tracks(
    limit=2,
    access=["playable,preview,blocked"],
    linked_partitioning=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

##### access: List[`str`]<a id="access-liststr"></a>

Filters content by level of access the user (logged in or anonymous) has to the track. The result list will include only tracks with the specified access. Include all options if you'd like to see all possible tracks. See `Track#access` schema for more details. 

##### linked_partitioning: `bool`<a id="linked_partitioning-bool"></a>

Returns paginated collection of items (recommended, returning a list without pagination is deprecated and should not be used)

#### 🔄 Return<a id="🔄-return"></a>

[`MeListLikedTracksResponse`](./soundcloud_python_sdk/pydantic/me_list_liked_tracks_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/likes/tracks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.me.list_playlists_info_tracks_owner`<a id="soundcloudmelist_playlists_info_tracks_owner"></a>

Returns playlist info, playlist tracks and tracks owner info.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_playlists_info_tracks_owner_response = (
    soundcloud.me.list_playlists_info_tracks_owner(
        show_tracks=True,
        linked_partitioning=True,
        limit=2,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### show_tracks: `bool`<a id="show_tracks-bool"></a>

A boolean flag to request a playlist with or without tracks. Default is `true`.

##### linked_partitioning: `bool`<a id="linked_partitioning-bool"></a>

Returns paginated collection of items (recommended, returning a list without pagination is deprecated and should not be used)

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

#### 🔄 Return<a id="🔄-return"></a>

[`MeGetLikedPlaylistsResponse`](./soundcloud_python_sdk/pydantic/me_get_liked_playlists_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/playlists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.me.list_user_tracks`<a id="soundcloudmelist_user_tracks"></a>

Returns a list of user's tracks.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_user_tracks_response = soundcloud.me.list_user_tracks(
    limit=2,
    linked_partitioning=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

##### linked_partitioning: `bool`<a id="linked_partitioning-bool"></a>

Returns paginated collection of items (recommended, returning a list without pagination is deprecated and should not be used)

#### 🔄 Return<a id="🔄-return"></a>

[`MeListLikedTracksResponse`](./soundcloud_python_sdk/pydantic/me_list_liked_tracks_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/tracks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.miscellaneous.resolve_soundcloud_urls`<a id="soundcloudmiscellaneousresolve_soundcloud_urls"></a>

Resolves soundcloud.com and on.soundcloud.com URLs to Resource URLs to use with the API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
soundcloud.miscellaneous.resolve_soundcloud_urls(
    url="https://soundcloud.com/user-434241656",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

SoundCloud URL

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resolve` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.oauth.authorize_user`<a id="soundcloudoauthauthorize_user"></a>

<h3>Security Advice</h3>
* [OAuth Authorization Code flow](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics-16#section-2.1.1) (`response_type=code`) is the only allowed method of authorization.
* Use the `state` parameter for [CSRF protection](https://tools.ietf.org/html/draft-ietf-oauth-security-topics-16#section-4.7). Pass a sufficient  random nonce here and verify this nonce again after retrieving the token.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
soundcloud.oauth.authorize_user(
    client_id="some client",
    redirect_uri="https://soundcloud.com",
    response_type="code",
    state="encrypted_session_info",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### client_id: `str`<a id="client_id-str"></a>

The client id belonging to your application

##### redirect_uri: `str`<a id="redirect_uri-str"></a>

The redirect uri you have configured for your application

##### response_type: `str`<a id="response_type-str"></a>

Support only the Authorization Code Flow

##### state: `str`<a id="state-str"></a>

Any value included here will be appended to the redirect URI. Use this for CSRF protection.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/connect` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.oauth.provision_access_token`<a id="soundcloudoauthprovision_access_token"></a>

This endpoint accepts POST requests and is used to provision access tokens once a user has authorized your application.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
soundcloud.oauth.provision_access_token(
    grant_type="authorization_code",
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    code="1-123456-12345678-FAbcfbe9ir2wdj0",
    redirect_uri="https://mywebsite/auth/soundcloud",
    refresh_token="1234c331329477150e7b6056ff212345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### grant_type: `str`<a id="grant_type-str"></a>

One of `authorization_code`, `client_credentials`, `refresh_token`

##### client_id: `str`<a id="client_id-str"></a>

Client ID

##### client_secret: `str`<a id="client_secret-str"></a>

Client secret

##### code: `str`<a id="code-str"></a>

Authorization code. Required on `grant_type = authorization_code`.

##### redirect_uri: `str`<a id="redirect_uri-str"></a>

Redirect URI. Required on `grant_type = (authorization_code|refresh_token)`.

##### refresh_token: `str`<a id="refresh_token-str"></a>

Refresh token. Required on `grant_type = refresh_token`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OAuthToken`](./soundcloud_python_sdk/type/o_auth_token.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/oauth2/token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.playlists.create_new_playlist`<a id="soundcloudplaylistscreate_new_playlist"></a>

Creates a playlist.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_playlist_response = soundcloud.playlists.create_new_playlist(
    playlist={
        "sharing": "public",
        "set_type": "album",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist: [`CreateUpdatePlaylistRequestPlaylist`](./soundcloud_python_sdk/type/create_update_playlist_request_playlist.py)<a id="playlist-createupdateplaylistrequestplaylistsoundcloud_python_sdktypecreate_update_playlist_request_playlistpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateUpdatePlaylistRequest`](./soundcloud_python_sdk/type/create_update_playlist_request.py)
Create Playlist request

#### 🔄 Return<a id="🔄-return"></a>

[`Playlist`](./soundcloud_python_sdk/pydantic/playlist.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.playlists.delete_playlist`<a id="soundcloudplaylistsdelete_playlist"></a>

Deletes a playlist.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
soundcloud.playlists.delete_playlist(
    playlist_id=10,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `int`<a id="playlist_id-int"></a>

SoundCloud playlist id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.playlists.get_playlist_by_id`<a id="soundcloudplaylistsget_playlist_by_id"></a>

Returns a playlist.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_playlist_by_id_response = soundcloud.playlists.get_playlist_by_id(
    playlist_id=1212781357,
    secret_token="string_example",
    access=["playable,preview"],
    show_tracks=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `int`<a id="playlist_id-int"></a>

SoundCloud playlist id

##### secret_token: `str`<a id="secret_token-str"></a>

A secret token to fetch private playlists/tracks

##### access: List[`str`]<a id="access-liststr"></a>

Filters content by level of access the user (logged in or anonymous) has to the track. The result list will include only tracks with the specified access. Include all options if you'd like to see all possible tracks. See `Track#access` schema for more details. 

##### show_tracks: `bool`<a id="show_tracks-bool"></a>

A boolean flag to request a playlist with or without tracks. Default is `true`.

#### 🔄 Return<a id="🔄-return"></a>

[`Playlist`](./soundcloud_python_sdk/pydantic/playlist.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.playlists.get_tracks`<a id="soundcloudplaylistsget_tracks"></a>

Returns tracks under a playlist.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tracks_response = soundcloud.playlists.get_tracks(
    playlist_id=1212781357,
    secret_token="string_example",
    access=["playable,preview"],
    linked_partitioning=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `int`<a id="playlist_id-int"></a>

SoundCloud playlist id

##### secret_token: `str`<a id="secret_token-str"></a>

A secret token to fetch private playlists/tracks

##### access: List[`str`]<a id="access-liststr"></a>

Filters content by level of access the user (logged in or anonymous) has to the track. The result list will include only tracks with the specified access. Include all options if you'd like to see all possible tracks. See `Track#access` schema for more details. 

##### linked_partitioning: `bool`<a id="linked_partitioning-bool"></a>

Returns paginated collection of items (recommended, returning a list without pagination is deprecated and should not be used)

#### 🔄 Return<a id="🔄-return"></a>

[`MeListLikedTracksResponse`](./soundcloud_python_sdk/pydantic/me_list_liked_tracks_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}/tracks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.playlists.list_reposters`<a id="soundcloudplaylistslist_reposters"></a>

Returns a collection of playlist's reposters.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_reposters_response = soundcloud.playlists.list_reposters(
    playlist_id=1212781357,
    limit=2,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `int`<a id="playlist_id-int"></a>

SoundCloud playlist id

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

#### 🔄 Return<a id="🔄-return"></a>

[`Users`](./soundcloud_python_sdk/pydantic/users.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}/reposters` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.playlists.update_playlist_by_id`<a id="soundcloudplaylistsupdate_playlist_by_id"></a>

Updates a playlist.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_playlist_by_id_response = soundcloud.playlists.update_playlist_by_id(
    playlist_id=10,
    playlist={
        "sharing": "public",
        "set_type": "album",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `int`<a id="playlist_id-int"></a>

SoundCloud playlist id

##### playlist: [`CreateUpdatePlaylistRequestPlaylist`](./soundcloud_python_sdk/type/create_update_playlist_request_playlist.py)<a id="playlist-createupdateplaylistrequestplaylistsoundcloud_python_sdktypecreate_update_playlist_request_playlistpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateUpdatePlaylistRequest`](./soundcloud_python_sdk/type/create_update_playlist_request.py)
Playlist payload

#### 🔄 Return<a id="🔄-return"></a>

[`Playlist`](./soundcloud_python_sdk/pydantic/playlist.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists/{playlist_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.reposts.playlist_as_authenticated_user`<a id="soundcloudrepostsplaylist_as_authenticated_user"></a>

Reposts a playlist as the authenticated user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
soundcloud.reposts.playlist_as_authenticated_user(
    playlist_id=1205584273,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `int`<a id="playlist_id-int"></a>

SoundCloud playlist id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/reposts/playlists/{playlist_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.reposts.remove_repost`<a id="soundcloudrepostsremove_repost"></a>

Removes a repost on a track as the authenticated user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
soundcloud.reposts.remove_repost(
    track_id=1015448728,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### track_id: `int`<a id="track_id-int"></a>

SoundCloud Track id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/reposts/tracks/{track_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.reposts.remove_repost_on_playlist`<a id="soundcloudrepostsremove_repost_on_playlist"></a>

Removes a repost on a playlist as the authenticated user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
soundcloud.reposts.remove_repost_on_playlist(
    playlist_id=1205584273,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### playlist_id: `int`<a id="playlist_id-int"></a>

SoundCloud playlist id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/reposts/playlists/{playlist_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.reposts.track_as_authenticated_user`<a id="soundcloudrepoststrack_as_authenticated_user"></a>

Reposts a track as the authenticated user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
soundcloud.reposts.track_as_authenticated_user(
    track_id=1015448728,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### track_id: `int`<a id="track_id-int"></a>

SoundCloud Track id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/reposts/tracks/{track_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.search.by_query`<a id="soundcloudsearchby_query"></a>

Performs a track search based on a query

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
by_query_response = soundcloud.search.by_query(
    q="hello",
    ids="1,2,3",
    genres="Pop,House",
    tags="test",
    bpm={
        "_from": 123,
        "to": 456,
    },
    duration={
        "_from": 123456,
        "to": 456789,
    },
    created_at={
        "_from": "2020-12-24 00:00:00",
        "to": "2020-12-26 00:00:00",
    },
    access=["playable,preview"],
    limit=2,
    offset=0,
    linked_partitioning=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

search

##### ids: `str`<a id="ids-str"></a>

A comma separated list of track ids to filter on

##### genres: `str`<a id="genres-str"></a>

A comma separated list of genres

##### tags: `str`<a id="tags-str"></a>

A comma separated list of tags

##### bpm: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./soundcloud_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="bpm-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonesoundcloud_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Return tracks with a specified bpm[from], bpm[to]

##### duration: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./soundcloud_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="duration-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonesoundcloud_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Return tracks within a specified duration range

##### created_at: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./soundcloud_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="created_at-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonesoundcloud_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

(yyyy-mm-dd hh:mm:ss) return tracks created within the specified dates

##### access: List[`str`]<a id="access-liststr"></a>

Filters content by level of access the user (logged in or anonymous) has to the track. The result list will include only tracks with the specified access. Include all options if you'd like to see all possible tracks. See `Track#access` schema for more details. 

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

##### offset: `int`<a id="offset-int"></a>

Offset of first result. Deprecated, use `linked_partitioning` instead.

##### linked_partitioning: `bool`<a id="linked_partitioning-bool"></a>

Returns paginated collection of items (recommended, returning a list without pagination is deprecated and should not be used)

#### 🔄 Return<a id="🔄-return"></a>

[`MeListLikedTracksResponse`](./soundcloud_python_sdk/pydantic/me_list_liked_tracks_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tracks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.search.by_query_0`<a id="soundcloudsearchby_query_0"></a>

Performs a playlist search based on a query

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
by_query_0_response = soundcloud.search.by_query_0(
    q="hello",
    access=["playable,preview"],
    show_tracks=True,
    limit=2,
    offset=0,
    linked_partitioning=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

search

##### access: List[`str`]<a id="access-liststr"></a>

Filters content by level of access the user (logged in or anonymous) has to the track. The result list will include only tracks with the specified access. Include all options if you'd like to see all possible tracks. See `Track#access` schema for more details. 

##### show_tracks: `bool`<a id="show_tracks-bool"></a>

A boolean flag to request a playlist with or without tracks. Default is `true`.

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

##### offset: `int`<a id="offset-int"></a>

Offset of first result. Deprecated, use `linked_partitioning` instead.

##### linked_partitioning: `bool`<a id="linked_partitioning-bool"></a>

Returns paginated collection of items (recommended, returning a list without pagination is deprecated and should not be used)

#### 🔄 Return<a id="🔄-return"></a>

[`MeGetLikedPlaylistsResponse`](./soundcloud_python_sdk/pydantic/me_get_liked_playlists_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/playlists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.search.user_query`<a id="soundcloudsearchuser_query"></a>

Performs a user search based on a query

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
user_query_response = soundcloud.search.user_query(
    q="hello",
    ids="1,2,3",
    limit=2,
    offset=0,
    linked_partitioning=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

search

##### ids: `str`<a id="ids-str"></a>

A comma separated list of track ids to filter on

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

##### offset: `int`<a id="offset-int"></a>

Offset of first result. Deprecated, use `linked_partitioning` instead.

##### linked_partitioning: `bool`<a id="linked_partitioning-bool"></a>

Returns paginated collection of items (recommended, returning a list without pagination is deprecated and should not be used)

#### 🔄 Return<a id="🔄-return"></a>

[`Users`](./soundcloud_python_sdk/pydantic/users.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.tracks.create_comment`<a id="soundcloudtrackscreate_comment"></a>

Returns the newly created comment on success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_comment_response = soundcloud.tracks.create_comment(
    track_id=308946187,
    comment={
        "body": "test comment",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### track_id: `int`<a id="track_id-int"></a>

SoundCloud Track id

##### comment: [`TracksCreateCommentRequestComment`](./soundcloud_python_sdk/type/tracks_create_comment_request_comment.py)<a id="comment-trackscreatecommentrequestcommentsoundcloud_python_sdktypetracks_create_comment_request_commentpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TracksCreateCommentRequest`](./soundcloud_python_sdk/type/tracks_create_comment_request.py)
Body of a comment 

#### 🔄 Return<a id="🔄-return"></a>

[`Comment`](./soundcloud_python_sdk/pydantic/comment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tracks/{track_id}/comments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.tracks.delete_track`<a id="soundcloudtracksdelete_track"></a>

Deletes a track.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
soundcloud.tracks.delete_track(
    track_id=308946187,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### track_id: `int`<a id="track_id-int"></a>

SoundCloud Track id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tracks/{track_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.tracks.get_by_id`<a id="soundcloudtracksget_by_id"></a>

Returns a track.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = soundcloud.tracks.get_by_id(
    track_id=308946187,
    secret_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### track_id: `int`<a id="track_id-int"></a>

SoundCloud Track id

##### secret_token: `str`<a id="secret_token-str"></a>

A secret token to fetch private playlists/tracks

#### 🔄 Return<a id="🔄-return"></a>

[`Track`](./soundcloud_python_sdk/pydantic/track.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tracks/{track_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.tracks.get_comments`<a id="soundcloudtracksget_comments"></a>

Returns the comments posted on the track(track_id).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_comments_response = soundcloud.tracks.get_comments(
    track_id=308946187,
    limit=2,
    offset=0,
    linked_partitioning=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### track_id: `int`<a id="track_id-int"></a>

SoundCloud Track id

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

##### offset: `int`<a id="offset-int"></a>

Offset of first result. Deprecated, use `linked_partitioning` instead.

##### linked_partitioning: `bool`<a id="linked_partitioning-bool"></a>

Returns paginated collection of items (recommended, returning a list without pagination is deprecated and should not be used)

#### 🔄 Return<a id="🔄-return"></a>

[`Comments`](./soundcloud_python_sdk/pydantic/comments.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tracks/{track_id}/comments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.tracks.get_favoriters`<a id="soundcloudtracksget_favoriters"></a>

Returns a list of users who have favorited or liked the track.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_favoriters_response = soundcloud.tracks.get_favoriters(
    track_id=308946187,
    limit=2,
    linked_partitioning=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### track_id: `int`<a id="track_id-int"></a>

SoundCloud Track id

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

##### linked_partitioning: `bool`<a id="linked_partitioning-bool"></a>

Returns paginated collection of items (recommended, returning a list without pagination is deprecated and should not be used)

#### 🔄 Return<a id="🔄-return"></a>

[`Users`](./soundcloud_python_sdk/pydantic/users.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tracks/{track_id}/favoriters` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.tracks.get_related_tracks`<a id="soundcloudtracksget_related_tracks"></a>

Returns all related tracks of track on SoundCloud.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_related_tracks_response = soundcloud.tracks.get_related_tracks(
    track_id=308946187,
    access=["playable,preview"],
    limit=2,
    offset=0,
    linked_partitioning=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### track_id: `int`<a id="track_id-int"></a>

SoundCloud Track id

##### access: List[`str`]<a id="access-liststr"></a>

Filters content by level of access the user (logged in or anonymous) has to the track. The result list will include only tracks with the specified access. Include all options if you'd like to see all possible tracks. See `Track#access` schema for more details. 

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

##### offset: `int`<a id="offset-int"></a>

Offset of first result. Deprecated, use `linked_partitioning` instead.

##### linked_partitioning: `bool`<a id="linked_partitioning-bool"></a>

Returns paginated collection of items (recommended, returning a list without pagination is deprecated and should not be used)

#### 🔄 Return<a id="🔄-return"></a>

[`MeListLikedTracksResponse`](./soundcloud_python_sdk/pydantic/me_list_liked_tracks_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tracks/{track_id}/related` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.tracks.get_streamable_urls`<a id="soundcloudtracksget_streamable_urls"></a>

Returns a track's streamable URLs

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_streamable_urls_response = soundcloud.tracks.get_streamable_urls(
    track_id=308946187,
    secret_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### track_id: `int`<a id="track_id-int"></a>

SoundCloud Track id

##### secret_token: `str`<a id="secret_token-str"></a>

A secret token to fetch private playlists/tracks

#### 🔄 Return<a id="🔄-return"></a>

[`Streams`](./soundcloud_python_sdk/pydantic/streams.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tracks/{track_id}/streams` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.tracks.list_reposters`<a id="soundcloudtrackslist_reposters"></a>

Returns a collection of track's reposters.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_reposters_response = soundcloud.tracks.list_reposters(
    track_id=308946187,
    limit=2,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### track_id: `int`<a id="track_id-int"></a>

SoundCloud Track id

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

#### 🔄 Return<a id="🔄-return"></a>

[`Users`](./soundcloud_python_sdk/pydantic/users.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tracks/{track_id}/reposters` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.tracks.update_track_information`<a id="soundcloudtracksupdate_track_information"></a>

Updates a track's information.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_track_information_response = soundcloud.tracks.update_track_information(
    track_id=308946187,
    track={
        "sharing": "public",
        "embeddable_by": "all",
        "streamable": True,
        "downloadable": True,
        "license": "no-rights-reserved",
        "commentable": True,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### track_id: `int`<a id="track_id-int"></a>

SoundCloud Track id

##### track: [`TrackMetadataRequestTrack`](./soundcloud_python_sdk/type/track_metadata_request_track.py)<a id="track-trackmetadatarequesttracksoundcloud_python_sdktypetrack_metadata_request_trackpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TrackMetadataRequest`](./soundcloud_python_sdk/type/track_metadata_request.py)
Track payload

#### 🔄 Return<a id="🔄-return"></a>

[`Track`](./soundcloud_python_sdk/pydantic/track.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tracks/{track_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.tracks.upload_new_track`<a id="soundcloudtracksupload_new_track"></a>

Uploads a new track.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_new_track_response = soundcloud.tracks.upload_new_track(
    body=None,
    track_title="string_example",
    track_asset_data=open("/path/to/file", "rb"),
    track_permalink="string_example",
    track_sharing="public",
    track_embeddable_by="all",
    track_purchase_url="string_example",
    track_description="string_example",
    track_genre="string_example",
    track_tag_list="string_example",
    track_label_name="string_example",
    track_release="string_example",
    track_release_date="string_example",
    track_streamable=True,
    track_downloadable=True,
    track_license="no-rights-reserved",
    track_commentable=True,
    track_isrc="string_example",
    track_artwork_data=open("/path/to/file", "rb"),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### track_title: `str`<a id="track_title-str"></a>

##### track_asset_data: `IO`<a id="track_asset_data-io"></a>

##### track_permalink: `str`<a id="track_permalink-str"></a>

##### track_sharing: `str`<a id="track_sharing-str"></a>

##### track_embeddable_by: `str`<a id="track_embeddable_by-str"></a>

who can embed this track \\\"all\\\", \\\"me\\\", or \\\"none\\\"

##### track_purchase_url: `str`<a id="track_purchase_url-str"></a>

##### track_description: `str`<a id="track_description-str"></a>

##### track_genre: `str`<a id="track_genre-str"></a>

##### track_tag_list: `str`<a id="track_tag_list-str"></a>

The tag_list property contains a list of tags separated by spaces. Multiword tags are quoted in double quotes. We also support machine tags that follow the pattern NAMESPACE:KEY=VALUE. For example: geo:lat=43.555 camel:size=medium “machine:tag=with space” Machine tags are not revealed to the user on the track pages.

##### track_label_name: `str`<a id="track_label_name-str"></a>

##### track_release: `str`<a id="track_release-str"></a>

##### track_release_date: `str`<a id="track_release_date-str"></a>

string, formatted as yyyy-mm-dd, representing release date

##### track_streamable: `bool`<a id="track_streamable-bool"></a>

##### track_downloadable: `bool`<a id="track_downloadable-bool"></a>

##### track_license: `str`<a id="track_license-str"></a>

Possible values: no-rights-reserved, all-rights-reserved, cc-by, cc-by-nc, cc-by-nd, cc-by-sa, cc-by-nc-nd, cc-by-nc-sa

##### track_commentable: `bool`<a id="track_commentable-bool"></a>

##### track_isrc: `str`<a id="track_isrc-str"></a>

##### track_artwork_data: `IO`<a id="track_artwork_data-io"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TracksUploadNewTrackRequest`](./soundcloud_python_sdk/type/tracks_upload_new_track_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Track`](./soundcloud_python_sdk/pydantic/track.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tracks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.users.get_followers`<a id="soundcloudusersget_followers"></a>

Returns a list of users that follows (user_id).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_followers_response = soundcloud.users.get_followers(
    user_id=948745750,
    limit=2,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `int`<a id="user_id-int"></a>

SoundCloud User id

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

#### 🔄 Return<a id="🔄-return"></a>

[`Users`](./soundcloud_python_sdk/pydantic/users.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}/followers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.users.get_following_by_id`<a id="soundcloudusersget_following_by_id"></a>

Returns (following_id) that is followed by (user_id).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_following_by_id_response = soundcloud.users.get_following_by_id(
    user_id=948745750,
    following_id=25219981,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `int`<a id="user_id-int"></a>

SoundCloud User id

##### following_id: `int`<a id="following_id-int"></a>

SoundCloud User id to denote a Following of a user

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./soundcloud_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}/followings/{following_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.users.get_user`<a id="soundcloudusersget_user"></a>

Returns a user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_response = soundcloud.users.get_user(
    user_id=948745750,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `int`<a id="user_id-int"></a>

SoundCloud User id

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./soundcloud_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.users.get_user_followings`<a id="soundcloudusersget_user_followings"></a>

Returns list of users that (user_id) follows.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_followings_response = soundcloud.users.get_user_followings(
    user_id=948745750,
    limit=2,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `int`<a id="user_id-int"></a>

SoundCloud User id

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

#### 🔄 Return<a id="🔄-return"></a>

[`Users`](./soundcloud_python_sdk/pydantic/users.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}/followings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.users.get_user_playlists`<a id="soundcloudusersget_user_playlists"></a>

Returns a list of user's playlists.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_playlists_response = soundcloud.users.get_user_playlists(
    user_id=948745750,
    access=["playable,preview"],
    show_tracks=True,
    limit=2,
    linked_partitioning=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `int`<a id="user_id-int"></a>

SoundCloud User id

##### access: List[`str`]<a id="access-liststr"></a>

Filters content by level of access the user (logged in or anonymous) has to the track. The result list will include only tracks with the specified access. Include all options if you'd like to see all possible tracks. See `Track#access` schema for more details. 

##### show_tracks: `bool`<a id="show_tracks-bool"></a>

A boolean flag to request a playlist with or without tracks. Default is `true`.

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

##### linked_partitioning: `bool`<a id="linked_partitioning-bool"></a>

Returns paginated collection of items (recommended, returning a list without pagination is deprecated and should not be used)

#### 🔄 Return<a id="🔄-return"></a>

[`MeGetLikedPlaylistsResponse`](./soundcloud_python_sdk/pydantic/me_get_liked_playlists_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}/playlists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.users.get_user_tracks`<a id="soundcloudusersget_user_tracks"></a>

Returns a list of user's tracks.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_tracks_response = soundcloud.users.get_user_tracks(
    user_id=948745750,
    access=["playable,preview"],
    limit=2,
    linked_partitioning=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `int`<a id="user_id-int"></a>

SoundCloud User id

##### access: List[`str`]<a id="access-liststr"></a>

Filters content by level of access the user (logged in or anonymous) has to the track. The result list will include only tracks with the specified access. Include all options if you'd like to see all possible tracks. See `Track#access` schema for more details. 

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

##### linked_partitioning: `bool`<a id="linked_partitioning-bool"></a>

Returns paginated collection of items (recommended, returning a list without pagination is deprecated and should not be used)

#### 🔄 Return<a id="🔄-return"></a>

[`MeListLikedTracksResponse`](./soundcloud_python_sdk/pydantic/me_list_liked_tracks_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}/tracks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.users.get_user_web_profiles`<a id="soundcloudusersget_user_web_profiles"></a>

Returns list of user's links added to their profile (website, facebook, instagram).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_web_profiles_response = soundcloud.users.get_user_web_profiles(
    user_id=948745750,
    limit=2,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `int`<a id="user_id-int"></a>

SoundCloud User id

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

#### 🔄 Return<a id="🔄-return"></a>

[`WebProfiles`](./soundcloud_python_sdk/pydantic/web_profiles.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}/web-profiles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.users.list_favorites`<a id="soundclouduserslist_favorites"></a>

Returns a list of user's favorited or liked tracks. (use /users/:userId/likes/tracks instead, to fetch a user's likes)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_favorites_response = soundcloud.users.list_favorites(
    user_id=948745750,
    limit=2,
    linked_partitioning=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `int`<a id="user_id-int"></a>

SoundCloud User id

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

##### linked_partitioning: `bool`<a id="linked_partitioning-bool"></a>

Returns paginated collection of items (recommended, returning a list without pagination is deprecated and should not be used)

#### 🔄 Return<a id="🔄-return"></a>

[`MeListLikedTracksResponse`](./soundcloud_python_sdk/pydantic/me_list_liked_tracks_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}/favorites` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.users.list_liked_playlists`<a id="soundclouduserslist_liked_playlists"></a>

Returns a list of user's liked playlists.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_liked_playlists_response = soundcloud.users.list_liked_playlists(
    user_id=948745750,
    limit=2,
    linked_partitioning=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `int`<a id="user_id-int"></a>

SoundCloud User id

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

##### linked_partitioning: `bool`<a id="linked_partitioning-bool"></a>

Returns paginated collection of items (recommended, returning a list without pagination is deprecated and should not be used)

#### 🔄 Return<a id="🔄-return"></a>

[`MeGetLikedPlaylistsResponse`](./soundcloud_python_sdk/pydantic/me_get_liked_playlists_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}/likes/playlists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `soundcloud.users.list_liked_tracks`<a id="soundclouduserslist_liked_tracks"></a>

Returns a list of user's liked tracks.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_liked_tracks_response = soundcloud.users.list_liked_tracks(
    user_id=948745750,
    access=["playable,preview"],
    limit=2,
    linked_partitioning=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `int`<a id="user_id-int"></a>

SoundCloud User id

##### access: List[`str`]<a id="access-liststr"></a>

Filters content by level of access the user (logged in or anonymous) has to the track. The result list will include only tracks with the specified access. Include all options if you'd like to see all possible tracks. See `Track#access` schema for more details. 

##### limit: `int`<a id="limit-int"></a>

Number of results to return in the collection.

##### linked_partitioning: `bool`<a id="linked_partitioning-bool"></a>

Returns paginated collection of items (recommended, returning a list without pagination is deprecated and should not be used)

#### 🔄 Return<a id="🔄-return"></a>

[`MeListLikedTracksResponse`](./soundcloud_python_sdk/pydantic/me_list_liked_tracks_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}/likes/tracks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
