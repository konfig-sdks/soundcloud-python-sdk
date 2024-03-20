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


class OAuthToken(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "grant_type",
            "client_secret",
            "client_id",
        }
        
        class properties:
            
            
            class grant_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "authorization_code": "AUTHORIZATION_CODE",
                        "refresh_token": "REFRESH_TOKEN",
                        "client_credentials": "CLIENT_CREDENTIALS",
                    }
                
                @schemas.classproperty
                def AUTHORIZATION_CODE(cls):
                    return cls("authorization_code")
                
                @schemas.classproperty
                def REFRESH_TOKEN(cls):
                    return cls("refresh_token")
                
                @schemas.classproperty
                def CLIENT_CREDENTIALS(cls):
                    return cls("client_credentials")
            client_id = schemas.StrSchema
            client_secret = schemas.StrSchema
            code = schemas.StrSchema
            redirect_uri = schemas.StrSchema
            refresh_token = schemas.StrSchema
            __annotations__ = {
                "grant_type": grant_type,
                "client_id": client_id,
                "client_secret": client_secret,
                "code": code,
                "redirect_uri": redirect_uri,
                "refresh_token": refresh_token,
            }
    
    grant_type: MetaOapg.properties.grant_type
    client_secret: MetaOapg.properties.client_secret
    client_id: MetaOapg.properties.client_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grant_type"]) -> MetaOapg.properties.grant_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_secret"]) -> MetaOapg.properties.client_secret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirect_uri"]) -> MetaOapg.properties.redirect_uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refresh_token"]) -> MetaOapg.properties.refresh_token: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["grant_type", "client_id", "client_secret", "code", "redirect_uri", "refresh_token", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grant_type"]) -> MetaOapg.properties.grant_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_secret"]) -> MetaOapg.properties.client_secret: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirect_uri"]) -> typing.Union[MetaOapg.properties.redirect_uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refresh_token"]) -> typing.Union[MetaOapg.properties.refresh_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["grant_type", "client_id", "client_secret", "code", "redirect_uri", "refresh_token", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        grant_type: typing.Union[MetaOapg.properties.grant_type, str, ],
        client_secret: typing.Union[MetaOapg.properties.client_secret, str, ],
        client_id: typing.Union[MetaOapg.properties.client_id, str, ],
        code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
        redirect_uri: typing.Union[MetaOapg.properties.redirect_uri, str, schemas.Unset] = schemas.unset,
        refresh_token: typing.Union[MetaOapg.properties.refresh_token, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OAuthToken':
        return super().__new__(
            cls,
            *args,
            grant_type=grant_type,
            client_secret=client_secret,
            client_id=client_id,
            code=code,
            redirect_uri=redirect_uri,
            refresh_token=refresh_token,
            _configuration=_configuration,
            **kwargs,
        )
