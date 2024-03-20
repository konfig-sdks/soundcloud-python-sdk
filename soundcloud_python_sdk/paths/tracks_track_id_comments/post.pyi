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

from soundcloud_python_sdk.model.too_many_requests import TooManyRequests as TooManyRequestsSchema
from soundcloud_python_sdk.model.comment import Comment as CommentSchema
from soundcloud_python_sdk.model.tracks_create_comment_request import TracksCreateCommentRequest as TracksCreateCommentRequestSchema
from soundcloud_python_sdk.model.tracks_create_comment_request_comment import TracksCreateCommentRequestComment as TracksCreateCommentRequestCommentSchema
from soundcloud_python_sdk.model.error import Error as ErrorSchema

from soundcloud_python_sdk.type.comment import Comment
from soundcloud_python_sdk.type.tracks_create_comment_request_comment import TracksCreateCommentRequestComment
from soundcloud_python_sdk.type.tracks_create_comment_request import TracksCreateCommentRequest
from soundcloud_python_sdk.type.too_many_requests import TooManyRequests
from soundcloud_python_sdk.type.error import Error

from ...api_client import Dictionary
from soundcloud_python_sdk.pydantic.tracks_create_comment_request import TracksCreateCommentRequest as TracksCreateCommentRequestPydantic
from soundcloud_python_sdk.pydantic.error import Error as ErrorPydantic
from soundcloud_python_sdk.pydantic.tracks_create_comment_request_comment import TracksCreateCommentRequestComment as TracksCreateCommentRequestCommentPydantic
from soundcloud_python_sdk.pydantic.too_many_requests import TooManyRequests as TooManyRequestsPydantic
from soundcloud_python_sdk.pydantic.comment import Comment as CommentPydantic

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
SchemaForRequestBodyApplicationJsonCharsetutf8 = TracksCreateCommentRequestSchema


request_body_tracks_create_comment_request = api_client.RequestBody(
    content={
        'application/json; charset=utf-8': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonCharsetutf8),
    },
    required=True,
)
SchemaFor201ResponseBodyApplicationJsonCharsetutf8 = CommentSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Comment


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Comment


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json; charset=utf-8': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJsonCharsetutf8),
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
SchemaFor429ResponseBodyApplicationJson = TooManyRequestsSchema


@dataclass
class ApiResponseFor429(api_client.ApiResponse):
    body: TooManyRequests


@dataclass
class ApiResponseFor429Async(api_client.AsyncApiResponse):
    body: TooManyRequests


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
    response_cls_async=ApiResponseFor429Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor429ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json; charset=utf-8',
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_comment_mapped_args(
        self,
        track_id: int,
        comment: typing.Optional[TracksCreateCommentRequestComment] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if comment is not None:
            _body["comment"] = comment
        args.body = _body
        if track_id is not None:
            _path_params["track_id"] = track_id
        args.path = _path_params
        return args

    async def _acreate_comment_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json; charset=utf-8',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Returns the newly created comment on success
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/tracks/{track_id}/comments',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_tracks_create_comment_request.serialize(body, content_type)
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


    def _create_comment_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json; charset=utf-8',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Returns the newly created comment on success
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/tracks/{track_id}/comments',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_tracks_create_comment_request.serialize(body, content_type)
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


class CreateCommentRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_comment(
        self,
        track_id: int,
        comment: typing.Optional[TracksCreateCommentRequestComment] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_comment_mapped_args(
            track_id=track_id,
            comment=comment,
        )
        return await self._acreate_comment_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def create_comment(
        self,
        track_id: int,
        comment: typing.Optional[TracksCreateCommentRequestComment] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_comment_mapped_args(
            track_id=track_id,
            comment=comment,
        )
        return self._create_comment_oapg(
            body=args.body,
            path_params=args.path,
        )

class CreateComment(BaseApi):

    async def acreate_comment(
        self,
        track_id: int,
        comment: typing.Optional[TracksCreateCommentRequestComment] = None,
        validate: bool = False,
        **kwargs,
    ) -> CommentPydantic:
        raw_response = await self.raw.acreate_comment(
            track_id=track_id,
            comment=comment,
            **kwargs,
        )
        if validate:
            return CommentPydantic(**raw_response.body)
        return api_client.construct_model_instance(CommentPydantic, raw_response.body)
    
    
    def create_comment(
        self,
        track_id: int,
        comment: typing.Optional[TracksCreateCommentRequestComment] = None,
        validate: bool = False,
    ) -> CommentPydantic:
        raw_response = self.raw.create_comment(
            track_id=track_id,
            comment=comment,
        )
        if validate:
            return CommentPydantic(**raw_response.body)
        return api_client.construct_model_instance(CommentPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        track_id: int,
        comment: typing.Optional[TracksCreateCommentRequestComment] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_comment_mapped_args(
            track_id=track_id,
            comment=comment,
        )
        return await self._acreate_comment_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        track_id: int,
        comment: typing.Optional[TracksCreateCommentRequestComment] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_comment_mapped_args(
            track_id=track_id,
            comment=comment,
        )
        return self._create_comment_oapg(
            body=args.body,
            path_params=args.path,
        )

