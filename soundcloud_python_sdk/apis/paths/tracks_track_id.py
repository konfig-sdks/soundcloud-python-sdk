from soundcloud_python_sdk.paths.tracks_track_id.get import ApiForget
from soundcloud_python_sdk.paths.tracks_track_id.put import ApiForput
from soundcloud_python_sdk.paths.tracks_track_id.delete import ApiFordelete


class TracksTrackId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
