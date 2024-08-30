# opthub_api_client.SolutionApi

All URIs are relative to *https://example.com/todo/opthub-api-endpoint*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_solution**](SolutionApi.md#create_solution) | **POST** /matches/{match_uuid}/solutions | Create solution
[**get_solution**](SolutionApi.md#get_solution) | **GET** /matches/{match_uuid}/trials/{trial_no}/solution | Retrieve a solution submitted by the participant themselves.


# **create_solution**
> CreateSolutionResponse create_solution(match_uuid, variable=variable)

Create solution

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import opthub_api_client
from opthub_api_client.models.create_solution_response import CreateSolutionResponse
from opthub_api_client.models.variable import Variable
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
    api_instance = opthub_api_client.SolutionApi(api_client)
    match_uuid = '5d7fc778-3e59-4128-a797-2e423c0aa461' # str | Match UUID
    variable = opthub_api_client.Variable() # Variable |  (optional)

    try:
        # Create solution
        api_response = api_instance.create_solution(match_uuid, variable=variable)
        print("The response of SolutionApi->create_solution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->create_solution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_uuid** | **str**| Match UUID | 
 **variable** | [**Variable**](Variable.md)|  | [optional] 

### Return type

[**CreateSolutionResponse**](CreateSolutionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information of the created Solution |  -  |
**404** | No such Match UUID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_solution**
> Solution get_solution(match_uuid, trial_no)

Retrieve a solution submitted by the participant themselves.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import opthub_api_client
from opthub_api_client.models.solution import Solution
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
    api_instance = opthub_api_client.SolutionApi(api_client)
    match_uuid = '5d7fc778-3e59-4128-a797-2e423c0aa461' # str | Match UUID
    trial_no = 4 # int | Trial number

    try:
        # Retrieve a solution submitted by the participant themselves.
        api_response = api_instance.get_solution(match_uuid, trial_no)
        print("The response of SolutionApi->get_solution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->get_solution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_uuid** | **str**| Match UUID | 
 **trial_no** | **int**| Trial number | 

### Return type

[**Solution**](Solution.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information of the Solution |  -  |
**404** | The trial specified in the query was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

