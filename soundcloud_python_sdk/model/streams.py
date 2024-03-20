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


class Streams(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            http_mp3_128_url = schemas.StrSchema
            hls_mp3_128_url = schemas.StrSchema
            hls_opus_64_url = schemas.StrSchema
            preview_mp3_128_url = schemas.StrSchema
            __annotations__ = {
                "http_mp3_128_url": http_mp3_128_url,
                "hls_mp3_128_url": hls_mp3_128_url,
                "hls_opus_64_url": hls_opus_64_url,
                "preview_mp3_128_url": preview_mp3_128_url,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["http_mp3_128_url"]) -> MetaOapg.properties.http_mp3_128_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hls_mp3_128_url"]) -> MetaOapg.properties.hls_mp3_128_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hls_opus_64_url"]) -> MetaOapg.properties.hls_opus_64_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preview_mp3_128_url"]) -> MetaOapg.properties.preview_mp3_128_url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["http_mp3_128_url", "hls_mp3_128_url", "hls_opus_64_url", "preview_mp3_128_url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["http_mp3_128_url"]) -> typing.Union[MetaOapg.properties.http_mp3_128_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hls_mp3_128_url"]) -> typing.Union[MetaOapg.properties.hls_mp3_128_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hls_opus_64_url"]) -> typing.Union[MetaOapg.properties.hls_opus_64_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preview_mp3_128_url"]) -> typing.Union[MetaOapg.properties.preview_mp3_128_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["http_mp3_128_url", "hls_mp3_128_url", "hls_opus_64_url", "preview_mp3_128_url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        http_mp3_128_url: typing.Union[MetaOapg.properties.http_mp3_128_url, str, schemas.Unset] = schemas.unset,
        hls_mp3_128_url: typing.Union[MetaOapg.properties.hls_mp3_128_url, str, schemas.Unset] = schemas.unset,
        hls_opus_64_url: typing.Union[MetaOapg.properties.hls_opus_64_url, str, schemas.Unset] = schemas.unset,
        preview_mp3_128_url: typing.Union[MetaOapg.properties.preview_mp3_128_url, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Streams':
        return super().__new__(
            cls,
            *args,
            http_mp3_128_url=http_mp3_128_url,
            hls_mp3_128_url=hls_mp3_128_url,
            hls_opus_64_url=hls_opus_64_url,
            preview_mp3_128_url=preview_mp3_128_url,
            _configuration=_configuration,
            **kwargs,
        )
