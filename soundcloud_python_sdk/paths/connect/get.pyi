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

from soundcloud_python_sdk.type.error import Error

from ...api_client import Dictionary
from soundcloud_python_sdk.pydantic.error import Error as ErrorPydantic

# Query params
ClientIdSchema = schemas.StrSchema
RedirectUriSchema = schemas.StrSchema


class ResponseTypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def CODE(cls):
        return cls("code")
StateSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'client_id': typing.Union[ClientIdSchema, str, ],
        'redirect_uri': typing.Union[RedirectUriSchema, str, ],
        'response_type': typing.Union[ResponseTypeSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'state': typing.Union[StateSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_client_id = api_client.QueryParameter(
    name="client_id",
    style=api_client.ParameterStyle.FORM,
    schema=ClientIdSchema,
    required=True,
    explode=True,
)
request_query_redirect_uri = api_client.QueryParameter(
    name="redirect_uri",
    style=api_client.ParameterStyle.FORM,
    schema=RedirectUriSchema,
    required=True,
    explode=True,
)
request_query_response_type = api_client.QueryParameter(
    name="response_type",
    style=api_client.ParameterStyle.FORM,
    schema=ResponseTypeSchema,
    required=True,
    explode=True,
)
request_query_state = api_client.QueryParameter(
    name="state",
    style=api_client.ParameterStyle.FORM,
    schema=StateSchema,
    explode=True,
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
)
LocationSchema = schemas.StrSchema
ResponseHeadersFor302 = typing_extensions.TypedDict(
    'ResponseHeadersFor302',
    {
        'Location': LocationSchema,
    }
)


@dataclass
class ApiResponseFor302(api_client.ApiResponse):
    headers: ResponseHeadersFor302
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor302Async(api_client.AsyncApiResponse):
    headers: ResponseHeadersFor302
    body: schemas.Unset = schemas.unset


_response_for_302 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor302,
    response_cls_async=ApiResponseFor302Async,
    headers=[
        location_parameter,
    ]
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

    def _authorize_user_mapped_args(
        self,
        client_id: str,
        redirect_uri: str,
        response_type: str,
        state: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if client_id is not None:
            _query_params["client_id"] = client_id
        if redirect_uri is not None:
            _query_params["redirect_uri"] = redirect_uri
        if response_type is not None:
            _query_params["response_type"] = response_type
        if state is not None:
            _query_params["state"] = state
        args.query = _query_params
        return args

    async def _aauthorize_user_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        The OAuth2 authorization endpoint. Your app redirects a user to this endpoint, allowing them to delegate access to their account.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_client_id,
            request_query_redirect_uri,
            request_query_response_type,
            request_query_state,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
            path_template='/connect',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _authorize_user_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        The OAuth2 authorization endpoint. Your app redirects a user to this endpoint, allowing them to delegate access to their account.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_client_id,
            request_query_redirect_uri,
            request_query_response_type,
            request_query_state,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
            path_template='/connect',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
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


class AuthorizeUserRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aauthorize_user(
        self,
        client_id: str,
        redirect_uri: str,
        response_type: str,
        state: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._authorize_user_mapped_args(
            client_id=client_id,
            redirect_uri=redirect_uri,
            response_type=response_type,
            state=state,
        )
        return await self._aauthorize_user_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def authorize_user(
        self,
        client_id: str,
        redirect_uri: str,
        response_type: str,
        state: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._authorize_user_mapped_args(
            client_id=client_id,
            redirect_uri=redirect_uri,
            response_type=response_type,
            state=state,
        )
        return self._authorize_user_oapg(
            query_params=args.query,
        )

class AuthorizeUser(BaseApi):

    async def aauthorize_user(
        self,
        client_id: str,
        redirect_uri: str,
        response_type: str,
        state: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aauthorize_user(
            client_id=client_id,
            redirect_uri=redirect_uri,
            response_type=response_type,
            state=state,
            **kwargs,
        )
    
    
    def authorize_user(
        self,
        client_id: str,
        redirect_uri: str,
        response_type: str,
        state: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.authorize_user(
            client_id=client_id,
            redirect_uri=redirect_uri,
            response_type=response_type,
            state=state,
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        client_id: str,
        redirect_uri: str,
        response_type: str,
        state: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._authorize_user_mapped_args(
            client_id=client_id,
            redirect_uri=redirect_uri,
            response_type=response_type,
            state=state,
        )
        return await self._aauthorize_user_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        client_id: str,
        redirect_uri: str,
        response_type: str,
        state: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._authorize_user_mapped_args(
            client_id=client_id,
            redirect_uri=redirect_uri,
            response_type=response_type,
            state=state,
        )
        return self._authorize_user_oapg(
            query_params=args.query,
        )

