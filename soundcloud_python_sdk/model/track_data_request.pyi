# coding: utf-8

"""
    SoundCloud Public API Specification

    Discover and play over 320 million music tracks. Join the world’s largest online community of artists, bands, DJs, and audio creators.

    The version of the OpenAPI document: 1.0.0
    Created by: https://github.com/soundcloud/api
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from soundcloud_python_sdk import schemas  # noqa: F401


class TrackDataRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            track_title = schemas.StrSchema
            track_asset_data = schemas.BinarySchema
            track_permalink = schemas.StrSchema
            
            
            class track_sharing(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PUBLIC(cls):
                    return cls("public")
                
                @schemas.classproperty
                def PRIVATE(cls):
                    return cls("private")
            
            
            class track_embeddable_by(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ALL(cls):
                    return cls("all")
                
                @schemas.classproperty
                def ME(cls):
                    return cls("me")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls("none")
            track_purchase_url = schemas.StrSchema
            track_description = schemas.StrSchema
            track_genre = schemas.StrSchema
            track_tag_list = schemas.StrSchema
            track_label_name = schemas.StrSchema
            track_release = schemas.StrSchema
            track_release_date = schemas.StrSchema
            track_streamable = schemas.BoolSchema
            track_downloadable = schemas.BoolSchema
            
            
            class track_license(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def NORIGHTSRESERVED(cls):
                    return cls("no-rights-reserved")
                
                @schemas.classproperty
                def ALLRIGHTSRESERVED(cls):
                    return cls("all-rights-reserved")
                
                @schemas.classproperty
                def CCBY(cls):
                    return cls("cc-by")
                
                @schemas.classproperty
                def CCBYNC(cls):
                    return cls("cc-by-nc")
                
                @schemas.classproperty
                def CCBYND(cls):
                    return cls("cc-by-nd")
                
                @schemas.classproperty
                def CCBYSA(cls):
                    return cls("cc-by-sa")
                
                @schemas.classproperty
                def CCBYNCND(cls):
                    return cls("cc-by-nc-nd")
                
                @schemas.classproperty
                def CCBYNCSA(cls):
                    return cls("cc-by-nc-sa")
            track_commentable = schemas.BoolSchema
            track_isrc = schemas.StrSchema
            track_artwork_data = schemas.BinarySchema
            __annotations__ = {
                "track[title]": track_title,
                "track[asset_data]": track_asset_data,
                "track[permalink]": track_permalink,
                "track[sharing]": track_sharing,
                "track[embeddable_by]": track_embeddable_by,
                "track[purchase_url]": track_purchase_url,
                "track[description]": track_description,
                "track[genre]": track_genre,
                "track[tag_list]": track_tag_list,
                "track[label_name]": track_label_name,
                "track[release]": track_release,
                "track[release_date]": track_release_date,
                "track[streamable]": track_streamable,
                "track[downloadable]": track_downloadable,
                "track[license]": track_license,
                "track[commentable]": track_commentable,
                "track[isrc]": track_isrc,
                "track[artwork_data]": track_artwork_data,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["track[title]"]) -> MetaOapg.properties.track_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["track[asset_data]"]) -> MetaOapg.properties.track_asset_data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["track[permalink]"]) -> MetaOapg.properties.track_permalink: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["track[sharing]"]) -> MetaOapg.properties.track_sharing: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["track[embeddable_by]"]) -> MetaOapg.properties.track_embeddable_by: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["track[purchase_url]"]) -> MetaOapg.properties.track_purchase_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["track[description]"]) -> MetaOapg.properties.track_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["track[genre]"]) -> MetaOapg.properties.track_genre: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["track[tag_list]"]) -> MetaOapg.properties.track_tag_list: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["track[label_name]"]) -> MetaOapg.properties.track_label_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["track[release]"]) -> MetaOapg.properties.track_release: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["track[release_date]"]) -> MetaOapg.properties.track_release_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["track[streamable]"]) -> MetaOapg.properties.track_streamable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["track[downloadable]"]) -> MetaOapg.properties.track_downloadable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["track[license]"]) -> MetaOapg.properties.track_license: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["track[commentable]"]) -> MetaOapg.properties.track_commentable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["track[isrc]"]) -> MetaOapg.properties.track_isrc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["track[artwork_data]"]) -> MetaOapg.properties.track_artwork_data: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["track[title]", "track[asset_data]", "track[permalink]", "track[sharing]", "track[embeddable_by]", "track[purchase_url]", "track[description]", "track[genre]", "track[tag_list]", "track[label_name]", "track[release]", "track[release_date]", "track[streamable]", "track[downloadable]", "track[license]", "track[commentable]", "track[isrc]", "track[artwork_data]", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["track[title]"]) -> typing.Union[MetaOapg.properties.track_title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["track[asset_data]"]) -> typing.Union[MetaOapg.properties.track_asset_data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["track[permalink]"]) -> typing.Union[MetaOapg.properties.track_permalink, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["track[sharing]"]) -> typing.Union[MetaOapg.properties.track_sharing, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["track[embeddable_by]"]) -> typing.Union[MetaOapg.properties.track_embeddable_by, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["track[purchase_url]"]) -> typing.Union[MetaOapg.properties.track_purchase_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["track[description]"]) -> typing.Union[MetaOapg.properties.track_description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["track[genre]"]) -> typing.Union[MetaOapg.properties.track_genre, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["track[tag_list]"]) -> typing.Union[MetaOapg.properties.track_tag_list, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["track[label_name]"]) -> typing.Union[MetaOapg.properties.track_label_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["track[release]"]) -> typing.Union[MetaOapg.properties.track_release, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["track[release_date]"]) -> typing.Union[MetaOapg.properties.track_release_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["track[streamable]"]) -> typing.Union[MetaOapg.properties.track_streamable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["track[downloadable]"]) -> typing.Union[MetaOapg.properties.track_downloadable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["track[license]"]) -> typing.Union[MetaOapg.properties.track_license, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["track[commentable]"]) -> typing.Union[MetaOapg.properties.track_commentable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["track[isrc]"]) -> typing.Union[MetaOapg.properties.track_isrc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["track[artwork_data]"]) -> typing.Union[MetaOapg.properties.track_artwork_data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["track[title]", "track[asset_data]", "track[permalink]", "track[sharing]", "track[embeddable_by]", "track[purchase_url]", "track[description]", "track[genre]", "track[tag_list]", "track[label_name]", "track[release]", "track[release_date]", "track[streamable]", "track[downloadable]", "track[license]", "track[commentable]", "track[isrc]", "track[artwork_data]", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TrackDataRequest':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
