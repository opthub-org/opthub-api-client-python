# CreateMatchTrialRequest

Solution space variable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variable** | [**ScalarOrVector**](ScalarOrVector.md) |  | [optional] 

## Example

```python
from opthub_api_client.models.create_match_trial_request import CreateMatchTrialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMatchTrialRequest from a JSON string
create_match_trial_request_instance = CreateMatchTrialRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMatchTrialRequest.to_json())

# convert the object into a dict
create_match_trial_request_dict = create_match_trial_request_instance.to_dict()
# create an instance of CreateMatchTrialRequest from a dict
create_match_trial_request_from_dict = CreateMatchTrialRequest.from_dict(create_match_trial_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


