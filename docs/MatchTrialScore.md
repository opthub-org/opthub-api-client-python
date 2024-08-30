# MatchTrialScore

Results of Score calculation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | The value of the Score | [optional] 
**started_at** | **datetime** | Score calculation start date and time | [optional] 
**finished_at** | **datetime** | Score calculation end date and time | [optional] 
**error** | **str** | Score calculation error information | [optional] 
**status** | [**RunnerStatus**](RunnerStatus.md) |  | 

## Example

```python
from opthub_api_client.models.match_trial_score import MatchTrialScore

# TODO update the JSON string below
json = "{}"
# create an instance of MatchTrialScore from a JSON string
match_trial_score_instance = MatchTrialScore.from_json(json)
# print the JSON string representation of the object
print(MatchTrialScore.to_json())

# convert the object into a dict
match_trial_score_dict = match_trial_score_instance.to_dict()
# create an instance of MatchTrialScore from a dict
match_trial_score_from_dict = MatchTrialScore.from_dict(match_trial_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


