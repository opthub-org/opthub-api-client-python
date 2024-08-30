# MatchTrialEvaluation

Evaluation results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objective** | **List[float]** | The value of the objective function | [optional] 
**constraint** | **object** | The value of the constraint condition | [optional] 
**feasible** | **bool** | Whether it is a feasible solution | [optional] 
**extra_info** | **object** | Auxiliary information for evaluation | [optional] 
**started_at** | **datetime** | Evaluation start date and time | [optional] 
**finished_at** | **datetime** | Evaluation end date and time | [optional] 
**error** | **str** | Evaluation error information | [optional] 
**status** | [**RunnerStatus**](RunnerStatus.md) |  | 

## Example

```python
from opthub_api_client.models.match_trial_evaluation import MatchTrialEvaluation

# TODO update the JSON string below
json = "{}"
# create an instance of MatchTrialEvaluation from a JSON string
match_trial_evaluation_instance = MatchTrialEvaluation.from_json(json)
# print the JSON string representation of the object
print(MatchTrialEvaluation.to_json())

# convert the object into a dict
match_trial_evaluation_dict = match_trial_evaluation_instance.to_dict()
# create an instance of MatchTrialEvaluation from a dict
match_trial_evaluation_from_dict = MatchTrialEvaluation.from_dict(match_trial_evaluation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


