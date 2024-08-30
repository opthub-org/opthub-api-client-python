# opthub_api_client.TrialApi

All URIs are relative to *https://example.com/todo/opthub-api-endpoint*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_match_trial**](TrialApi.md#get_match_trial) | **GET** /matches/{match_uuid}/trials/{trial_no} | Retrieve status of a specific Trial related to the Solution submitted by the Participant themselves.


# **get_match_trial**
> MatchTrialStatus get_match_trial(match_uuid, trial_no)

Retrieve status of a specific Trial related to the Solution submitted by the Participant themselves.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import opthub_api_client
from opthub_api_client.models.match_trial_status import MatchTrialStatus
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
    api_instance = opthub_api_client.TrialApi(api_client)
    match_uuid = '5d7fc778-3e59-4128-a797-2e423c0aa461' # str | Match UUID
    trial_no = 4 # int | Trial number

    try:
        # Retrieve status of a specific Trial related to the Solution submitted by the Participant themselves.
        api_response = api_instance.get_match_trial(match_uuid, trial_no)
        print("The response of TrialApi->get_match_trial:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrialApi->get_match_trial: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_uuid** | **str**| Match UUID | 
 **trial_no** | **int**| Trial number | 

### Return type

[**MatchTrialStatus**](MatchTrialStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status information of the Trial |  -  |
**404** | The trial specified in the query was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

