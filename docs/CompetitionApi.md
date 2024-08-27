# opthub_api_client.CompetitionApi

All URIs are relative to *https://example.com/todo/opthub-api-endpoint*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resolve_competition_alias_by_id**](CompetitionApi.md#resolve_competition_alias_by_id) | **GET** /competition/{id}/alias | Retrieve the competition alias from the competition ID
[**resolve_competition_id_by_alias**](CompetitionApi.md#resolve_competition_id_by_alias) | **GET** /competition/alias/{alias} | Retrieve the competition ID from the competition alias


# **resolve_competition_alias_by_id**
> str resolve_competition_alias_by_id(id)

Retrieve the competition alias from the competition ID

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
    api_instance = opthub_api_client.CompetitionApi(api_client)
    id = '42c999a1-a30c-47ef-b656-eb49f67488dc' # str | Competition ID

    try:
        # Retrieve the competition alias from the competition ID
        api_response = api_instance.resolve_competition_alias_by_id(id)
        print("The response of CompetitionApi->resolve_competition_alias_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompetitionApi->resolve_competition_alias_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Competition ID | 

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
**200** | Competition alias |  -  |
**404** | Competition not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_competition_id_by_alias**
> str resolve_competition_id_by_alias(alias)

Retrieve the competition ID from the competition alias

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
    api_instance = opthub_api_client.CompetitionApi(api_client)
    alias = 'competition123' # str | Competition alias

    try:
        # Retrieve the competition ID from the competition alias
        api_response = api_instance.resolve_competition_id_by_alias(alias)
        print("The response of CompetitionApi->resolve_competition_id_by_alias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompetitionApi->resolve_competition_id_by_alias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Competition alias | 

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
**200** | Competition ID |  -  |
**404** | Competition not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

