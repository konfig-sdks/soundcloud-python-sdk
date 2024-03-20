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
from soundcloud_python_sdk.model.track_metadata_request_track import TrackMetadataRequestTrack as TrackMetadataRequestTrackSchema
from soundcloud_python_sdk.model.track_metadata_request import TrackMetadataRequest as TrackMetadataRequestSchema
from soundcloud_python_sdk.model.track_data_request import TrackDataRequest as TrackDataRequestSchema
from soundcloud_python_sdk.model.error import Error as ErrorSchema

from soundcloud_python_sdk.type.track_data_request import TrackDataRequest
from soundcloud_python_sdk.type.track_metadata_request_track import TrackMetadataRequestTrack
from soundcloud_python_sdk.type.track_metadata_request import TrackMetadataRequest
from soundcloud_python_sdk.type.track import Track
from soundcloud_python_sdk.type.error import Error

from ...api_client import Dictionary
from soundcloud_python_sdk.pydantic.error import Error as ErrorPydantic
from soundcloud_python_sdk.pydantic.track_metadata_request_track import TrackMetadataRequestTrack as TrackMetadataRequestTrackPydantic
from soundcloud_python_sdk.pydantic.track import Track as TrackPydantic
from soundcloud_python_sdk.pydantic.track_metadata_request import TrackMetadataRequest as TrackMetadataRequestPydantic
from soundcloud_python_sdk.pydantic.track_data_request import TrackDataRequest as TrackDataRequestPydantic

# Path params
TrackIdSchema = schemas.IntSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'track_id': typing.Union[TrackIdSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_track_id = api_client.PathParameter(
    name="track_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TrackIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = TrackMetadataRequestSchema
SchemaForRequestBodyMultipartFormData = TrackDataRequestSchema
SchemaForRequestBodyMultipartXWwwFormUrlencoded = TrackDataRequestSchema


request_body_track_metadata_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
        'multipart/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartXWwwFormUrlencoded),
    },
)
SchemaFor200ResponseBodyApplicationJsonCharsetutf8 = TrackSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Track


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Track


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json; charset=utf-8': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonCharsetutf8),
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
_all_accept_content_types = (
    'application/json; charset=utf-8',
)


class BaseApi(api_client.Api):

    def _update_track_information_mapped_args(
        self,
        track_id: int,
        track: typing.Optional[TrackMetadataRequestTrack] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if track is not None:
            _body["track"] = track
        args.body = _body
        if track_id is not None:
            _path_params["track_id"] = track_id
        args.path = _path_params
        return args

    async def _aupdate_track_information_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Updates a track&#x27;s information.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_track_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/tracks/{track_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_track_metadata_request.serialize(body, content_type)
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


    def _update_track_information_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Updates a track&#x27;s information.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_track_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/tracks/{track_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_track_metadata_request.serialize(body, content_type)
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


class UpdateTrackInformationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_track_information(
        self,
        track_id: int,
        track: typing.Optional[TrackMetadataRequestTrack] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_track_information_mapped_args(
            track_id=track_id,
            track=track,
        )
        return await self._aupdate_track_information_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_track_information(
        self,
        track_id: int,
        track: typing.Optional[TrackMetadataRequestTrack] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_track_information_mapped_args(
            track_id=track_id,
            track=track,
        )
        return self._update_track_information_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateTrackInformation(BaseApi):

    async def aupdate_track_information(
        self,
        track_id: int,
        track: typing.Optional[TrackMetadataRequestTrack] = None,
        validate: bool = False,
        **kwargs,
    ) -> TrackPydantic:
        raw_response = await self.raw.aupdate_track_information(
            track_id=track_id,
            track=track,
            **kwargs,
        )
        if validate:
            return TrackPydantic(**raw_response.body)
        return api_client.construct_model_instance(TrackPydantic, raw_response.body)
    
    
    def update_track_information(
        self,
        track_id: int,
        track: typing.Optional[TrackMetadataRequestTrack] = None,
        validate: bool = False,
    ) -> TrackPydantic:
        raw_response = self.raw.update_track_information(
            track_id=track_id,
            track=track,
        )
        if validate:
            return TrackPydantic(**raw_response.body)
        return api_client.construct_model_instance(TrackPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        track_id: int,
        track: typing.Optional[TrackMetadataRequestTrack] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_track_information_mapped_args(
            track_id=track_id,
            track=track,
        )
        return await self._aupdate_track_information_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        track_id: int,
        track: typing.Optional[TrackMetadataRequestTrack] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_track_information_mapped_args(
            track_id=track_id,
            track=track,
        )
        return self._update_track_information_oapg(
            body=args.body,
            path_params=args.path,
        )

