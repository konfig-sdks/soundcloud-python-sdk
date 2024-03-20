# coding: utf-8

"""
    SoundCloud Public API Specification

    Discover and play over 320 million music tracks. Join the world’s largest online community of artists, bands, DJs, and audio creators.

    The version of the OpenAPI document: 1.0.0
    Created by: https://github.com/soundcloud/api
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from soundcloud_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from soundcloud_python_sdk.api_response import AsyncGeneratorResponse
from soundcloud_python_sdk import api_client, exceptions
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

from soundcloud_python_sdk.model.track import Track as TrackSchema
from soundcloud_python_sdk.model.tracks_upload_new_track_request1 import TracksUploadNewTrackRequest1 as TracksUploadNewTrackRequest1Schema
from soundcloud_python_sdk.model.error import Error as ErrorSchema
from soundcloud_python_sdk.model.tracks_upload_new_track_request import TracksUploadNewTrackRequest as TracksUploadNewTrackRequestSchema

from soundcloud_python_sdk.type.tracks_upload_new_track_request1 import TracksUploadNewTrackRequest1
from soundcloud_python_sdk.type.tracks_upload_new_track_request import TracksUploadNewTrackRequest
from soundcloud_python_sdk.type.track import Track
from soundcloud_python_sdk.type.error import Error

from ...api_client import Dictionary
from soundcloud_python_sdk.pydantic.error import Error as ErrorPydantic
from soundcloud_python_sdk.pydantic.tracks_upload_new_track_request import TracksUploadNewTrackRequest as TracksUploadNewTrackRequestPydantic
from soundcloud_python_sdk.pydantic.track import Track as TrackPydantic
from soundcloud_python_sdk.pydantic.tracks_upload_new_track_request1 import TracksUploadNewTrackRequest1 as TracksUploadNewTrackRequest1Pydantic

# body param
SchemaForRequestBodyMultipartFormData = TracksUploadNewTrackRequestSchema
SchemaForRequestBodyMultipartXWwwFormUrlencoded = TracksUploadNewTrackRequest1Schema


request_body_tracks_upload_new_track_request = api_client.RequestBody(
    content={
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
        'multipart/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartXWwwFormUrlencoded),
    },
)
SchemaFor201ResponseBodyApplicationJsonCharsetutf8 = TrackSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Track


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Track


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json; charset=utf-8': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJsonCharsetutf8),
    },
)
SchemaFor400ResponseBodyApplicationJsonCharsetutf8 = ErrorSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: Error


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json; charset=utf-8': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJsonCharsetutf8),
    },
)
SchemaFor401ResponseBodyApplicationJsonCharsetutf8 = ErrorSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: Error


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json; charset=utf-8': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJsonCharsetutf8),
    },
)
SchemaFor422ResponseBodyApplicationJson = ErrorSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: Error


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json; charset=utf-8',
    'application/json',
)


class BaseApi(api_client.Api):

    def _upload_new_track_mapped_args(
        self,
        track_title: typing.Optional[str] = None,
        track_asset_data: typing.Optional[typing.IO] = None,
        track_permalink: typing.Optional[str] = None,
        track_sharing: typing.Optional[str] = None,
        track_embeddable_by: typing.Optional[str] = None,
        track_purchase_url: typing.Optional[str] = None,
        track_description: typing.Optional[str] = None,
        track_genre: typing.Optional[str] = None,
        track_tag_list: typing.Optional[str] = None,
        track_label_name: typing.Optional[str] = None,
        track_release: typing.Optional[str] = None,
        track_release_date: typing.Optional[str] = None,
        track_streamable: typing.Optional[bool] = None,
        track_downloadable: typing.Optional[bool] = None,
        track_license: typing.Optional[str] = None,
        track_commentable: typing.Optional[bool] = None,
        track_isrc: typing.Optional[str] = None,
        track_artwork_data: typing.Optional[typing.IO] = None,
        body: typing.Optional[TracksUploadNewTrackRequest] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if track_title is not None:
            _body["track[title]"] = track_title
        if track_asset_data is not None:
            _body["track[asset_data]"] = track_asset_data
        if track_permalink is not None:
            _body["track[permalink]"] = track_permalink
        if track_sharing is not None:
            _body["track[sharing]"] = track_sharing
        if track_embeddable_by is not None:
            _body["track[embeddable_by]"] = track_embeddable_by
        if track_purchase_url is not None:
            _body["track[purchase_url]"] = track_purchase_url
        if track_description is not None:
            _body["track[description]"] = track_description
        if track_genre is not None:
            _body["track[genre]"] = track_genre
        if track_tag_list is not None:
            _body["track[tag_list]"] = track_tag_list
        if track_label_name is not None:
            _body["track[label_name]"] = track_label_name
        if track_release is not None:
            _body["track[release]"] = track_release
        if track_release_date is not None:
            _body["track[release_date]"] = track_release_date
        if track_streamable is not None:
            _body["track[streamable]"] = track_streamable
        if track_downloadable is not None:
            _body["track[downloadable]"] = track_downloadable
        if track_license is not None:
            _body["track[license]"] = track_license
        if track_commentable is not None:
            _body["track[commentable]"] = track_commentable
        if track_isrc is not None:
            _body["track[isrc]"] = track_isrc
        if track_artwork_data is not None:
            _body["track[artwork_data]"] = track_artwork_data
        args.body = body if body is not None else _body
        return args

    async def _aupload_new_track_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Uploads a new track.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/tracks',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_tracks_upload_new_track_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _upload_new_track_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Uploads a new track.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/tracks',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_tracks_upload_new_track_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class UploadNewTrackRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupload_new_track(
        self,
        track_title: typing.Optional[str] = None,
        track_asset_data: typing.Optional[typing.IO] = None,
        track_permalink: typing.Optional[str] = None,
        track_sharing: typing.Optional[str] = None,
        track_embeddable_by: typing.Optional[str] = None,
        track_purchase_url: typing.Optional[str] = None,
        track_description: typing.Optional[str] = None,
        track_genre: typing.Optional[str] = None,
        track_tag_list: typing.Optional[str] = None,
        track_label_name: typing.Optional[str] = None,
        track_release: typing.Optional[str] = None,
        track_release_date: typing.Optional[str] = None,
        track_streamable: typing.Optional[bool] = None,
        track_downloadable: typing.Optional[bool] = None,
        track_license: typing.Optional[str] = None,
        track_commentable: typing.Optional[bool] = None,
        track_isrc: typing.Optional[str] = None,
        track_artwork_data: typing.Optional[typing.IO] = None,
        body: typing.Optional[TracksUploadNewTrackRequest] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._upload_new_track_mapped_args(
            body=body,
            track_title=track_title,
            track_asset_data=track_asset_data,
            track_permalink=track_permalink,
            track_sharing=track_sharing,
            track_embeddable_by=track_embeddable_by,
            track_purchase_url=track_purchase_url,
            track_description=track_description,
            track_genre=track_genre,
            track_tag_list=track_tag_list,
            track_label_name=track_label_name,
            track_release=track_release,
            track_release_date=track_release_date,
            track_streamable=track_streamable,
            track_downloadable=track_downloadable,
            track_license=track_license,
            track_commentable=track_commentable,
            track_isrc=track_isrc,
            track_artwork_data=track_artwork_data,
        )
        return await self._aupload_new_track_oapg(
            body=args.body,
            **kwargs,
        )
    
    def upload_new_track(
        self,
        track_title: typing.Optional[str] = None,
        track_asset_data: typing.Optional[typing.IO] = None,
        track_permalink: typing.Optional[str] = None,
        track_sharing: typing.Optional[str] = None,
        track_embeddable_by: typing.Optional[str] = None,
        track_purchase_url: typing.Optional[str] = None,
        track_description: typing.Optional[str] = None,
        track_genre: typing.Optional[str] = None,
        track_tag_list: typing.Optional[str] = None,
        track_label_name: typing.Optional[str] = None,
        track_release: typing.Optional[str] = None,
        track_release_date: typing.Optional[str] = None,
        track_streamable: typing.Optional[bool] = None,
        track_downloadable: typing.Optional[bool] = None,
        track_license: typing.Optional[str] = None,
        track_commentable: typing.Optional[bool] = None,
        track_isrc: typing.Optional[str] = None,
        track_artwork_data: typing.Optional[typing.IO] = None,
        body: typing.Optional[TracksUploadNewTrackRequest] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._upload_new_track_mapped_args(
            body=body,
            track_title=track_title,
            track_asset_data=track_asset_data,
            track_permalink=track_permalink,
            track_sharing=track_sharing,
            track_embeddable_by=track_embeddable_by,
            track_purchase_url=track_purchase_url,
            track_description=track_description,
            track_genre=track_genre,
            track_tag_list=track_tag_list,
            track_label_name=track_label_name,
            track_release=track_release,
            track_release_date=track_release_date,
            track_streamable=track_streamable,
            track_downloadable=track_downloadable,
            track_license=track_license,
            track_commentable=track_commentable,
            track_isrc=track_isrc,
            track_artwork_data=track_artwork_data,
        )
        return self._upload_new_track_oapg(
            body=args.body,
        )

class UploadNewTrack(BaseApi):

    async def aupload_new_track(
        self,
        track_title: typing.Optional[str] = None,
        track_asset_data: typing.Optional[typing.IO] = None,
        track_permalink: typing.Optional[str] = None,
        track_sharing: typing.Optional[str] = None,
        track_embeddable_by: typing.Optional[str] = None,
        track_purchase_url: typing.Optional[str] = None,
        track_description: typing.Optional[str] = None,
        track_genre: typing.Optional[str] = None,
        track_tag_list: typing.Optional[str] = None,
        track_label_name: typing.Optional[str] = None,
        track_release: typing.Optional[str] = None,
        track_release_date: typing.Optional[str] = None,
        track_streamable: typing.Optional[bool] = None,
        track_downloadable: typing.Optional[bool] = None,
        track_license: typing.Optional[str] = None,
        track_commentable: typing.Optional[bool] = None,
        track_isrc: typing.Optional[str] = None,
        track_artwork_data: typing.Optional[typing.IO] = None,
        body: typing.Optional[TracksUploadNewTrackRequest] = None,
        validate: bool = False,
        **kwargs,
    ) -> TrackPydantic:
        raw_response = await self.raw.aupload_new_track(
            body=body,
            track_title=track_title,
            track_asset_data=track_asset_data,
            track_permalink=track_permalink,
            track_sharing=track_sharing,
            track_embeddable_by=track_embeddable_by,
            track_purchase_url=track_purchase_url,
            track_description=track_description,
            track_genre=track_genre,
            track_tag_list=track_tag_list,
            track_label_name=track_label_name,
            track_release=track_release,
            track_release_date=track_release_date,
            track_streamable=track_streamable,
            track_downloadable=track_downloadable,
            track_license=track_license,
            track_commentable=track_commentable,
            track_isrc=track_isrc,
            track_artwork_data=track_artwork_data,
            **kwargs,
        )
        if validate:
            return TrackPydantic(**raw_response.body)
        return api_client.construct_model_instance(TrackPydantic, raw_response.body)
    
    
    def upload_new_track(
        self,
        track_title: typing.Optional[str] = None,
        track_asset_data: typing.Optional[typing.IO] = None,
        track_permalink: typing.Optional[str] = None,
        track_sharing: typing.Optional[str] = None,
        track_embeddable_by: typing.Optional[str] = None,
        track_purchase_url: typing.Optional[str] = None,
        track_description: typing.Optional[str] = None,
        track_genre: typing.Optional[str] = None,
        track_tag_list: typing.Optional[str] = None,
        track_label_name: typing.Optional[str] = None,
        track_release: typing.Optional[str] = None,
        track_release_date: typing.Optional[str] = None,
        track_streamable: typing.Optional[bool] = None,
        track_downloadable: typing.Optional[bool] = None,
        track_license: typing.Optional[str] = None,
        track_commentable: typing.Optional[bool] = None,
        track_isrc: typing.Optional[str] = None,
        track_artwork_data: typing.Optional[typing.IO] = None,
        body: typing.Optional[TracksUploadNewTrackRequest] = None,
        validate: bool = False,
    ) -> TrackPydantic:
        raw_response = self.raw.upload_new_track(
            body=body,
            track_title=track_title,
            track_asset_data=track_asset_data,
            track_permalink=track_permalink,
            track_sharing=track_sharing,
            track_embeddable_by=track_embeddable_by,
            track_purchase_url=track_purchase_url,
            track_description=track_description,
            track_genre=track_genre,
            track_tag_list=track_tag_list,
            track_label_name=track_label_name,
            track_release=track_release,
            track_release_date=track_release_date,
            track_streamable=track_streamable,
            track_downloadable=track_downloadable,
            track_license=track_license,
            track_commentable=track_commentable,
            track_isrc=track_isrc,
            track_artwork_data=track_artwork_data,
        )
        if validate:
            return TrackPydantic(**raw_response.body)
        return api_client.construct_model_instance(TrackPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        track_title: typing.Optional[str] = None,
        track_asset_data: typing.Optional[typing.IO] = None,
        track_permalink: typing.Optional[str] = None,
        track_sharing: typing.Optional[str] = None,
        track_embeddable_by: typing.Optional[str] = None,
        track_purchase_url: typing.Optional[str] = None,
        track_description: typing.Optional[str] = None,
        track_genre: typing.Optional[str] = None,
        track_tag_list: typing.Optional[str] = None,
        track_label_name: typing.Optional[str] = None,
        track_release: typing.Optional[str] = None,
        track_release_date: typing.Optional[str] = None,
        track_streamable: typing.Optional[bool] = None,
        track_downloadable: typing.Optional[bool] = None,
        track_license: typing.Optional[str] = None,
        track_commentable: typing.Optional[bool] = None,
        track_isrc: typing.Optional[str] = None,
        track_artwork_data: typing.Optional[typing.IO] = None,
        body: typing.Optional[TracksUploadNewTrackRequest] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._upload_new_track_mapped_args(
            body=body,
            track_title=track_title,
            track_asset_data=track_asset_data,
            track_permalink=track_permalink,
            track_sharing=track_sharing,
            track_embeddable_by=track_embeddable_by,
            track_purchase_url=track_purchase_url,
            track_description=track_description,
            track_genre=track_genre,
            track_tag_list=track_tag_list,
            track_label_name=track_label_name,
            track_release=track_release,
            track_release_date=track_release_date,
            track_streamable=track_streamable,
            track_downloadable=track_downloadable,
            track_license=track_license,
            track_commentable=track_commentable,
            track_isrc=track_isrc,
            track_artwork_data=track_artwork_data,
        )
        return await self._aupload_new_track_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        track_title: typing.Optional[str] = None,
        track_asset_data: typing.Optional[typing.IO] = None,
        track_permalink: typing.Optional[str] = None,
        track_sharing: typing.Optional[str] = None,
        track_embeddable_by: typing.Optional[str] = None,
        track_purchase_url: typing.Optional[str] = None,
        track_description: typing.Optional[str] = None,
        track_genre: typing.Optional[str] = None,
        track_tag_list: typing.Optional[str] = None,
        track_label_name: typing.Optional[str] = None,
        track_release: typing.Optional[str] = None,
        track_release_date: typing.Optional[str] = None,
        track_streamable: typing.Optional[bool] = None,
        track_downloadable: typing.Optional[bool] = None,
        track_license: typing.Optional[str] = None,
        track_commentable: typing.Optional[bool] = None,
        track_isrc: typing.Optional[str] = None,
        track_artwork_data: typing.Optional[typing.IO] = None,
        body: typing.Optional[TracksUploadNewTrackRequest] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._upload_new_track_mapped_args(
            body=body,
            track_title=track_title,
            track_asset_data=track_asset_data,
            track_permalink=track_permalink,
            track_sharing=track_sharing,
            track_embeddable_by=track_embeddable_by,
            track_purchase_url=track_purchase_url,
            track_description=track_description,
            track_genre=track_genre,
            track_tag_list=track_tag_list,
            track_label_name=track_label_name,
            track_release=track_release,
            track_release_date=track_release_date,
            track_streamable=track_streamable,
            track_downloadable=track_downloadable,
            track_license=track_license,
            track_commentable=track_commentable,
            track_isrc=track_isrc,
            track_artwork_data=track_artwork_data,
        )
        return self._upload_new_track_oapg(
            body=args.body,
        )

