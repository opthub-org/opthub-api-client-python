# MatchTrialStatus

Match Trial status information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**MatchTrialStatusType**](MatchTrialStatusType.md) |  | 
**evaluation** | [**MatchTrialEvaluation**](MatchTrialEvaluation.md) |  | [optional] 
**score** | [**MatchTrialScore**](MatchTrialScore.md) |  | [optional] 

## Example

```python
from opthub_api_client.models.match_trial_status import MatchTrialStatus

# TODO update the JSON string below
json = "{}"
# create an instance of MatchTrialStatus from a JSON string
match_trial_status_instance = MatchTrialStatus.from_json(json)
# print the JSON string representation of the object
print(MatchTrialStatus.to_json())

# convert the object into a dict
match_trial_status_dict = match_trial_status_instance.to_dict()
# create an instance of MatchTrialStatus from a dict
match_trial_status_from_dict = MatchTrialStatus.from_dict(match_trial_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


