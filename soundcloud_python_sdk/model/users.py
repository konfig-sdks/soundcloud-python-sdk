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


class Users(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class collection(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['User']:
                        return User
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['User'], typing.List['User']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'collection':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'User':
                    return super().__getitem__(i)
            next_href = schemas.StrSchema
            __annotations__ = {
                "collection": collection,
                "next_href": next_href,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collection"]) -> MetaOapg.properties.collection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_href"]) -> MetaOapg.properties.next_href: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["collection", "next_href", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collection"]) -> typing.Union[MetaOapg.properties.collection, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_href"]) -> typing.Union[MetaOapg.properties.next_href, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["collection", "next_href", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        collection: typing.Union[MetaOapg.properties.collection, list, tuple, schemas.Unset] = schemas.unset,
        next_href: typing.Union[MetaOapg.properties.next_href, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Users':
        return super().__new__(
            cls,
            *args,
            collection=collection,
            next_href=next_href,
            _configuration=_configuration,
            **kwargs,
        )

from soundcloud_python_sdk.model.user import User
