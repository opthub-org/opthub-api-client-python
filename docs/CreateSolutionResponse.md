# CreateSolutionResponse

解の作成リクエストの結果

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participant** | [**Participant**](Participant.md) |  | [optional] 
**trial_no** | **int** | 試行番号 | 

## Example

```python
from opthub_api_client.models.create_solution_response import CreateSolutionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSolutionResponse from a JSON string
create_solution_response_instance = CreateSolutionResponse.from_json(json)
# print the JSON string representation of the object
print(CreateSolutionResponse.to_json())

# convert the object into a dict
create_solution_response_dict = create_solution_response_instance.to_dict()
# create an instance of CreateSolutionResponse from a dict
create_solution_response_from_dict = CreateSolutionResponse.from_dict(create_solution_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


