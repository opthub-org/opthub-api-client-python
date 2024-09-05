# opthub_api_client.MatchTrialsApi

All URIs are relative to *https://api.opthub.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_match_trial**](MatchTrialsApi.md#create_match_trial) | **POST** /matches/{match_uuid}/trials | Create a match trial
[**get_match_evaluation**](MatchTrialsApi.md#get_match_evaluation) | **GET** /matches/{match_uuid}/trials/{trial_no}/evaluation | Retrieve status of a specific match evaluation related to the Solution submitted by the Participant themselves.
[**get_match_score**](MatchTrialsApi.md#get_match_score) | **GET** /matches/{match_uuid}/trials/{trial_no}/score | Retrieve status of a specific match score related to the Solution submitted by the Participant themselves.
[**get_match_trial**](MatchTrialsApi.md#get_match_trial) | **GET** /matches/{match_uuid}/trials/{trial_no} | Retrieve status of a specific Match Trial related to the Solution submitted by the Participant themselves.
[**get_solution**](MatchTrialsApi.md#get_solution) | **GET** /matches/{match_uuid}/trials/{trial_no}/solution | Retrieve the Solution submitted by the Participant themselves.


# **create_match_trial**
> MatchTrialResponse create_match_trial(match_uuid, create_match_trial_request=create_match_trial_request)

Create a match trial

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import opthub_api_client
from opthub_api_client.models.create_match_trial_request import CreateMatchTrialRequest
from opthub_api_client.models.match_trial_response import MatchTrialResponse
from opthub_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.opthub.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = opthub_api_client.Configuration(
    host = "https://api.opthub.ai"
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
    api_instance = opthub_api_client.MatchTrialsApi(api_client)
    match_uuid = '5d7fc778-3e59-4128-a797-2e423c0aa461' # str | Match UUID
    create_match_trial_request = opthub_api_client.CreateMatchTrialRequest() # CreateMatchTrialRequest |  (optional)

    try:
        # Create a match trial
        api_response = api_instance.create_match_trial(match_uuid, create_match_trial_request=create_match_trial_request)
        print("The response of MatchTrialsApi->create_match_trial:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchTrialsApi->create_match_trial: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_uuid** | **str**| Match UUID | 
 **create_match_trial_request** | [**CreateMatchTrialRequest**](CreateMatchTrialRequest.md)|  | [optional] 

### Return type

[**MatchTrialResponse**](MatchTrialResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information of the created match trial |  -  |
**400** | Bad request input |  -  |
**401** | Authentication error |  -  |
**403** | Forbidden operation |  -  |
**404** | The entry specified in the query was not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_match_evaluation**
> MatchTrialEvaluation get_match_evaluation(match_uuid, trial_no)

Retrieve status of a specific match evaluation related to the Solution submitted by the Participant themselves.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import opthub_api_client
from opthub_api_client.models.match_trial_evaluation import MatchTrialEvaluation
from opthub_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.opthub.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = opthub_api_client.Configuration(
    host = "https://api.opthub.ai"
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
    api_instance = opthub_api_client.MatchTrialsApi(api_client)
    match_uuid = '5d7fc778-3e59-4128-a797-2e423c0aa461' # str | Match UUID
    trial_no = 4 # int | Trial number

    try:
        # Retrieve status of a specific match evaluation related to the Solution submitted by the Participant themselves.
        api_response = api_instance.get_match_evaluation(match_uuid, trial_no)
        print("The response of MatchTrialsApi->get_match_evaluation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchTrialsApi->get_match_evaluation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_uuid** | **str**| Match UUID | 
 **trial_no** | **int**| Trial number | 

### Return type

[**MatchTrialEvaluation**](MatchTrialEvaluation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status information of the match trial |  -  |
**400** | Bad request input |  -  |
**401** | Authentication error |  -  |
**403** | Forbidden operation |  -  |
**404** | The entry specified in the query was not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_match_score**
> MatchTrialScore get_match_score(match_uuid, trial_no)

Retrieve status of a specific match score related to the Solution submitted by the Participant themselves.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import opthub_api_client
from opthub_api_client.models.match_trial_score import MatchTrialScore
from opthub_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.opthub.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = opthub_api_client.Configuration(
    host = "https://api.opthub.ai"
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
    api_instance = opthub_api_client.MatchTrialsApi(api_client)
    match_uuid = '5d7fc778-3e59-4128-a797-2e423c0aa461' # str | Match UUID
    trial_no = 4 # int | Trial number

    try:
        # Retrieve status of a specific match score related to the Solution submitted by the Participant themselves.
        api_response = api_instance.get_match_score(match_uuid, trial_no)
        print("The response of MatchTrialsApi->get_match_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchTrialsApi->get_match_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_uuid** | **str**| Match UUID | 
 **trial_no** | **int**| Trial number | 

### Return type

[**MatchTrialScore**](MatchTrialScore.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status information of the match trial |  -  |
**400** | Bad request input |  -  |
**401** | Authentication error |  -  |
**403** | Forbidden operation |  -  |
**404** | The entry specified in the query was not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_match_trial**
> MatchTrialResponse get_match_trial(match_uuid, trial_no)

Retrieve status of a specific Match Trial related to the Solution submitted by the Participant themselves.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import opthub_api_client
from opthub_api_client.models.match_trial_response import MatchTrialResponse
from opthub_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.opthub.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = opthub_api_client.Configuration(
    host = "https://api.opthub.ai"
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
    api_instance = opthub_api_client.MatchTrialsApi(api_client)
    match_uuid = '5d7fc778-3e59-4128-a797-2e423c0aa461' # str | Match UUID
    trial_no = 4 # int | Trial number

    try:
        # Retrieve status of a specific Match Trial related to the Solution submitted by the Participant themselves.
        api_response = api_instance.get_match_trial(match_uuid, trial_no)
        print("The response of MatchTrialsApi->get_match_trial:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchTrialsApi->get_match_trial: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_uuid** | **str**| Match UUID | 
 **trial_no** | **int**| Trial number | 

### Return type

[**MatchTrialResponse**](MatchTrialResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status information of the match trial |  -  |
**400** | Bad request input |  -  |
**401** | Authentication error |  -  |
**403** | Forbidden operation |  -  |
**404** | The entry specified in the query was not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_solution**
> Solution get_solution(match_uuid, trial_no)

Retrieve the Solution submitted by the Participant themselves.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import opthub_api_client
from opthub_api_client.models.solution import Solution
from opthub_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.opthub.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = opthub_api_client.Configuration(
    host = "https://api.opthub.ai"
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
    api_instance = opthub_api_client.MatchTrialsApi(api_client)
    match_uuid = '5d7fc778-3e59-4128-a797-2e423c0aa461' # str | Match UUID
    trial_no = 4 # int | Trial number

    try:
        # Retrieve the Solution submitted by the Participant themselves.
        api_response = api_instance.get_solution(match_uuid, trial_no)
        print("The response of MatchTrialsApi->get_solution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchTrialsApi->get_solution: %s\n" % e)
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
**200** | Solution information |  -  |
**400** | Bad request input |  -  |
**401** | Authentication error |  -  |
**403** | Forbidden operation |  -  |
**404** | The entry specified in the query was not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

