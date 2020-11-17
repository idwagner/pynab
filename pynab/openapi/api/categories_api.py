# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pynab.openapi.api_client import ApiClient
from pynab.openapi.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class CategoriesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_categories(self, budget_id, **kwargs):  # noqa: E501
        """List categories  # noqa: E501

        Returns all categories grouped by category group.  Amounts (budgeted, activity, balance, etc.) are specific to the current budget month (UTC).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_categories(budget_id, async_req=True)
        >>> result = thread.get()

        :param budget_id: The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). (required)
        :type budget_id: str
        :param last_knowledge_of_server: The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.
        :type last_knowledge_of_server: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CategoriesResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_categories_with_http_info(budget_id, **kwargs)  # noqa: E501

    def get_categories_with_http_info(self, budget_id, **kwargs):  # noqa: E501
        """List categories  # noqa: E501

        Returns all categories grouped by category group.  Amounts (budgeted, activity, balance, etc.) are specific to the current budget month (UTC).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_categories_with_http_info(budget_id, async_req=True)
        >>> result = thread.get()

        :param budget_id: The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). (required)
        :type budget_id: str
        :param last_knowledge_of_server: The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.
        :type last_knowledge_of_server: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CategoriesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'budget_id',
            'last_knowledge_of_server'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_categories" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'budget_id' is set
        if self.api_client.client_side_validation and ('budget_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['budget_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `budget_id` when calling `get_categories`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'budget_id' in local_var_params:
            path_params['budget_id'] = local_var_params['budget_id']  # noqa: E501

        query_params = []
        if 'last_knowledge_of_server' in local_var_params and local_var_params['last_knowledge_of_server'] is not None:  # noqa: E501
            query_params.append(('last_knowledge_of_server', local_var_params['last_knowledge_of_server']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501
        
        response_types_map = {
            200: "CategoriesResponse",
            404: "ErrorResponse",
        }

        return self.api_client.call_api(
            '/budgets/{budget_id}/categories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_category_by_id(self, budget_id, category_id, **kwargs):  # noqa: E501
        """Single category  # noqa: E501

        Returns a single category.  Amounts (budgeted, activity, balance, etc.) are specific to the current budget month (UTC).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_category_by_id(budget_id, category_id, async_req=True)
        >>> result = thread.get()

        :param budget_id: The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). (required)
        :type budget_id: str
        :param category_id: The id of the category (required)
        :type category_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CategoryResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_category_by_id_with_http_info(budget_id, category_id, **kwargs)  # noqa: E501

    def get_category_by_id_with_http_info(self, budget_id, category_id, **kwargs):  # noqa: E501
        """Single category  # noqa: E501

        Returns a single category.  Amounts (budgeted, activity, balance, etc.) are specific to the current budget month (UTC).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_category_by_id_with_http_info(budget_id, category_id, async_req=True)
        >>> result = thread.get()

        :param budget_id: The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). (required)
        :type budget_id: str
        :param category_id: The id of the category (required)
        :type category_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CategoryResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'budget_id',
            'category_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_category_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'budget_id' is set
        if self.api_client.client_side_validation and ('budget_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['budget_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `budget_id` when calling `get_category_by_id`")  # noqa: E501
        # verify the required parameter 'category_id' is set
        if self.api_client.client_side_validation and ('category_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['category_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `category_id` when calling `get_category_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'budget_id' in local_var_params:
            path_params['budget_id'] = local_var_params['budget_id']  # noqa: E501
        if 'category_id' in local_var_params:
            path_params['category_id'] = local_var_params['category_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501
        
        response_types_map = {
            200: "CategoryResponse",
            404: "ErrorResponse",
        }

        return self.api_client.call_api(
            '/budgets/{budget_id}/categories/{category_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_month_category_by_id(self, budget_id, month, category_id, **kwargs):  # noqa: E501
        """Single category for a specific budget month  # noqa: E501

        Returns a single category for a specific budget month.  Amounts (budgeted, activity, balance, etc.) are specific to the current budget month (UTC).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_month_category_by_id(budget_id, month, category_id, async_req=True)
        >>> result = thread.get()

        :param budget_id: The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). (required)
        :type budget_id: str
        :param month: The budget month in ISO format (e.g. 2016-12-01) (\"current\" can also be used to specify the current calendar month (UTC)) (required)
        :type month: date
        :param category_id: The id of the category (required)
        :type category_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CategoryResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_month_category_by_id_with_http_info(budget_id, month, category_id, **kwargs)  # noqa: E501

    def get_month_category_by_id_with_http_info(self, budget_id, month, category_id, **kwargs):  # noqa: E501
        """Single category for a specific budget month  # noqa: E501

        Returns a single category for a specific budget month.  Amounts (budgeted, activity, balance, etc.) are specific to the current budget month (UTC).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_month_category_by_id_with_http_info(budget_id, month, category_id, async_req=True)
        >>> result = thread.get()

        :param budget_id: The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). (required)
        :type budget_id: str
        :param month: The budget month in ISO format (e.g. 2016-12-01) (\"current\" can also be used to specify the current calendar month (UTC)) (required)
        :type month: date
        :param category_id: The id of the category (required)
        :type category_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CategoryResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'budget_id',
            'month',
            'category_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_month_category_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'budget_id' is set
        if self.api_client.client_side_validation and ('budget_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['budget_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `budget_id` when calling `get_month_category_by_id`")  # noqa: E501
        # verify the required parameter 'month' is set
        if self.api_client.client_side_validation and ('month' not in local_var_params or  # noqa: E501
                                                        local_var_params['month'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `month` when calling `get_month_category_by_id`")  # noqa: E501
        # verify the required parameter 'category_id' is set
        if self.api_client.client_side_validation and ('category_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['category_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `category_id` when calling `get_month_category_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'budget_id' in local_var_params:
            path_params['budget_id'] = local_var_params['budget_id']  # noqa: E501
        if 'month' in local_var_params:
            path_params['month'] = local_var_params['month']  # noqa: E501
        if 'category_id' in local_var_params:
            path_params['category_id'] = local_var_params['category_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501
        
        response_types_map = {
            200: "CategoryResponse",
            404: "ErrorResponse",
        }

        return self.api_client.call_api(
            '/budgets/{budget_id}/months/{month}/categories/{category_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def update_month_category(self, budget_id, month, category_id, data, **kwargs):  # noqa: E501
        """Update a category for a specific month  # noqa: E501

        Update a category for a specific month.  Only `budgeted` amount can be updated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_month_category(budget_id, month, category_id, data, async_req=True)
        >>> result = thread.get()

        :param budget_id: The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). (required)
        :type budget_id: str
        :param month: The budget month in ISO format (e.g. 2016-12-01) (\"current\" can also be used to specify the current calendar month (UTC)) (required)
        :type month: date
        :param category_id: The id of the category (required)
        :type category_id: str
        :param data: The category to update.  Only `budgeted` amount can be updated and any other fields specified will be ignored. (required)
        :type data: SaveMonthCategoryWrapper
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SaveCategoryResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.update_month_category_with_http_info(budget_id, month, category_id, data, **kwargs)  # noqa: E501

    def update_month_category_with_http_info(self, budget_id, month, category_id, data, **kwargs):  # noqa: E501
        """Update a category for a specific month  # noqa: E501

        Update a category for a specific month.  Only `budgeted` amount can be updated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_month_category_with_http_info(budget_id, month, category_id, data, async_req=True)
        >>> result = thread.get()

        :param budget_id: The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). (required)
        :type budget_id: str
        :param month: The budget month in ISO format (e.g. 2016-12-01) (\"current\" can also be used to specify the current calendar month (UTC)) (required)
        :type month: date
        :param category_id: The id of the category (required)
        :type category_id: str
        :param data: The category to update.  Only `budgeted` amount can be updated and any other fields specified will be ignored. (required)
        :type data: SaveMonthCategoryWrapper
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SaveCategoryResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'budget_id',
            'month',
            'category_id',
            'data'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_month_category" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'budget_id' is set
        if self.api_client.client_side_validation and ('budget_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['budget_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `budget_id` when calling `update_month_category`")  # noqa: E501
        # verify the required parameter 'month' is set
        if self.api_client.client_side_validation and ('month' not in local_var_params or  # noqa: E501
                                                        local_var_params['month'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `month` when calling `update_month_category`")  # noqa: E501
        # verify the required parameter 'category_id' is set
        if self.api_client.client_side_validation and ('category_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['category_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `category_id` when calling `update_month_category`")  # noqa: E501
        # verify the required parameter 'data' is set
        if self.api_client.client_side_validation and ('data' not in local_var_params or  # noqa: E501
                                                        local_var_params['data'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data` when calling `update_month_category`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'budget_id' in local_var_params:
            path_params['budget_id'] = local_var_params['budget_id']  # noqa: E501
        if 'month' in local_var_params:
            path_params['month'] = local_var_params['month']  # noqa: E501
        if 'category_id' in local_var_params:
            path_params['category_id'] = local_var_params['category_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in local_var_params:
            body_params = local_var_params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501
        
        response_types_map = {
            200: "SaveCategoryResponse",
            400: "ErrorResponse",
        }

        return self.api_client.call_api(
            '/budgets/{budget_id}/months/{month}/categories/{category_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))