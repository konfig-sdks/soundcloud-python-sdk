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


class ActivitiesCollection(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['ActivitiesCollectionItem']:
            return ActivitiesCollectionItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['ActivitiesCollectionItem'], typing.List['ActivitiesCollectionItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ActivitiesCollection':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'ActivitiesCollectionItem':
        return super().__getitem__(i)

from soundcloud_python_sdk.model.activities_collection_item import ActivitiesCollectionItem
