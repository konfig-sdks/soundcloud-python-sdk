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

from soundcloud_python_sdk.model.error import Error as ErrorSchema
from soundcloud_python_sdk.model.user import User as UserSchema

from soundcloud_python_sdk.type.user import User
from soundcloud_python_sdk.type.error import Error

from ...api_client import Dictionary
from soundcloud_python_sdk.pydantic.error import Error as ErrorPydantic
from soundcloud_python_sdk.pydantic.user import User as UserPydantic

# Path params
UserIdSchema = schemas.IntSchema
FollowingIdSchema = schemas.IntSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'user_id': typing.Union[UserIdSchema, decimal.Decimal, int, ],
        'following_id': typing.Union[FollowingIdSchema, decimal.Decimal, int, ],
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


request_path_user_id = api_client.PathParameter(
    name="user_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=UserIdSchema,
    required=True,
)
request_path_following_id = api_client.PathParameter(
    name="following_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=FollowingIdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJsonCharsetutf8 = UserSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: User


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: User


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json; charset=utf-8': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonCharsetutf8),
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
SchemaFor404ResponseBodyApplicationJson = ErrorSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: Error


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json; charset=utf-8',
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_following_by_id_mapped_args(
        self,
        user_id: int,
        following_id: int,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if user_id is not None:
            _path_params["user_id"] = user_id
        if following_id is not None:
            _path_params["following_id"] = following_id
        args.path = _path_params
        return args

    async def _aget_following_by_id_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Returns a user&#x27;s following. (use /users/{user_id} instead, to fetch the user details)
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_user_id,
            request_path_following_id,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/users/{user_id}/followings/{following_id}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _get_following_by_id_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Returns a user&#x27;s following. (use /users/{user_id} instead, to fetch the user details)
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_user_id,
            request_path_following_id,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/users/{user_id}/followings/{following_id}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class GetFollowingByIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @api_client.DeprecationWarningOnce(prefix="users")
    async def aget_following_by_id(
        self,
        user_id: int,
        following_id: int,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_following_by_id_mapped_args(
            user_id=user_id,
            following_id=following_id,
        )
        return await self._aget_following_by_id_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="users")
    def get_following_by_id(
        self,
        user_id: int,
        following_id: int,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_following_by_id_mapped_args(
            user_id=user_id,
            following_id=following_id,
        )
        return self._get_following_by_id_oapg(
            path_params=args.path,
        )

class GetFollowingById(BaseApi):

    @api_client.DeprecationWarningOnce(prefix="users")
    async def aget_following_by_id(
        self,
        user_id: int,
        following_id: int,
        validate: bool = False,
        **kwargs,
    ) -> UserPydantic:
        raw_response = await self.raw.aget_following_by_id(
            user_id=user_id,
            following_id=following_id,
            **kwargs,
        )
        if validate:
            return UserPydantic(**raw_response.body)
        return api_client.construct_model_instance(UserPydantic, raw_response.body)
    
    
    @api_client.DeprecationWarningOnce(prefix="users")
    def get_following_by_id(
        self,
        user_id: int,
        following_id: int,
        validate: bool = False,
    ) -> UserPydantic:
        raw_response = self.raw.get_following_by_id(
            user_id=user_id,
            following_id=following_id,
        )
        if validate:
            return UserPydantic(**raw_response.body)
        return api_client.construct_model_instance(UserPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @api_client.DeprecationWarningOnce(prefix="users")
    async def aget(
        self,
        user_id: int,
        following_id: int,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_following_by_id_mapped_args(
            user_id=user_id,
            following_id=following_id,
        )
        return await self._aget_following_by_id_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="users")
    def get(
        self,
        user_id: int,
        following_id: int,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_following_by_id_mapped_args(
            user_id=user_id,
            following_id=following_id,
        )
        return self._get_following_by_id_oapg(
            path_params=args.path,
        )

