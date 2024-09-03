# MatchTrialResponse

Information of the created Solution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trial_no** | **int** | Trial number | 
**status** | [**MatchTrialStatus**](MatchTrialStatus.md) |  | 
**created_at** | **datetime** | Creation date and time | 

## Example

```python
from opthub_api_client.models.match_trial_response import MatchTrialResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MatchTrialResponse from a JSON string
match_trial_response_instance = MatchTrialResponse.from_json(json)
# print the JSON string representation of the object
print(MatchTrialResponse.to_json())

# convert the object into a dict
match_trial_response_dict = match_trial_response_instance.to_dict()
# create an instance of MatchTrialResponse from a dict
match_trial_response_from_dict = MatchTrialResponse.from_dict(match_trial_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


