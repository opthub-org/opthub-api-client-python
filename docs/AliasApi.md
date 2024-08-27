# opthub_api_client.AliasApi

All URIs are relative to *https://example.com/todo/opthub-api-endpoint*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resolve_competition_alias_by_id**](AliasApi.md#resolve_competition_alias_by_id) | **GET** /competition/{id}/alias | コンペティションIDからコンペティションのエイリアスを取得
[**resolve_competition_id_by_alias**](AliasApi.md#resolve_competition_id_by_alias) | **GET** /competition/alias/{alias} | コンペティションのエイリアスからコンペティションIDを取得
[**resolve_match_alias_by_id**](AliasApi.md#resolve_match_alias_by_id) | **GET** /competition/match/{matchId}/alias | 競技IDから競技のエイリアスを取得
[**resolve_match_id_by_alias**](AliasApi.md#resolve_match_id_by_alias) | **GET** /competition/match/alias/{alias} | 競技のエイリアスから競技IDを取得


# **resolve_competition_alias_by_id**
> str resolve_competition_alias_by_id(id)

コンペティションIDからコンペティションのエイリアスを取得

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import opthub_api_client
from opthub_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://example.com/todo/opthub-api-endpoint
# See configuration.py for a list of all supported configuration parameters.
configuration = opthub_api_client.Configuration(
    host = "https://example.com/todo/opthub-api-endpoint"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with opthub_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opthub_api_client.AliasApi(api_client)
    id = 'id_example' # str | コンペティションのID

    try:
        # コンペティションIDからコンペティションのエイリアスを取得
        api_response = api_instance.resolve_competition_alias_by_id(id)
        print("The response of AliasApi->resolve_competition_alias_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AliasApi->resolve_competition_alias_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| コンペティションのID | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_competition_id_by_alias**
> str resolve_competition_id_by_alias(alias)

コンペティションのエイリアスからコンペティションIDを取得

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import opthub_api_client
from opthub_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://example.com/todo/opthub-api-endpoint
# See configuration.py for a list of all supported configuration parameters.
configuration = opthub_api_client.Configuration(
    host = "https://example.com/todo/opthub-api-endpoint"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with opthub_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opthub_api_client.AliasApi(api_client)
    alias = 'alias_example' # str | コンペティションのエイリアス

    try:
        # コンペティションのエイリアスからコンペティションIDを取得
        api_response = api_instance.resolve_competition_id_by_alias(alias)
        print("The response of AliasApi->resolve_competition_id_by_alias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AliasApi->resolve_competition_id_by_alias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| コンペティションのエイリアス | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_match_alias_by_id**
> str resolve_match_alias_by_id(match_id)

競技IDから競技のエイリアスを取得

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import opthub_api_client
from opthub_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://example.com/todo/opthub-api-endpoint
# See configuration.py for a list of all supported configuration parameters.
configuration = opthub_api_client.Configuration(
    host = "https://example.com/todo/opthub-api-endpoint"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with opthub_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opthub_api_client.AliasApi(api_client)
    match_id = 'match_id_example' # str | 競技のID

    try:
        # 競技IDから競技のエイリアスを取得
        api_response = api_instance.resolve_match_alias_by_id(match_id)
        print("The response of AliasApi->resolve_match_alias_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AliasApi->resolve_match_alias_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **str**| 競技のID | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_match_id_by_alias**
> str resolve_match_id_by_alias(alias)

競技のエイリアスから競技IDを取得

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import opthub_api_client
from opthub_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://example.com/todo/opthub-api-endpoint
# See configuration.py for a list of all supported configuration parameters.
configuration = opthub_api_client.Configuration(
    host = "https://example.com/todo/opthub-api-endpoint"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with opthub_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opthub_api_client.AliasApi(api_client)
    alias = 'alias_example' # str | 競技のエイリアス

    try:
        # 競技のエイリアスから競技IDを取得
        api_response = api_instance.resolve_match_id_by_alias(alias)
        print("The response of AliasApi->resolve_match_id_by_alias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AliasApi->resolve_match_id_by_alias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| 競技のエイリアス | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

