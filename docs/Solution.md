# Solution

Solution information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variable** | **List[float]** | Solution space variable | 
**created_at** | **datetime** | Creation date and time | 
**user_id** | **str** | ID of the user who created it | [optional] 

## Example

```python
from opthub_api_client.models.solution import Solution

# TODO update the JSON string below
json = "{}"
# create an instance of Solution from a JSON string
solution_instance = Solution.from_json(json)
# print the JSON string representation of the object
print(Solution.to_json())

# convert the object into a dict
solution_dict = solution_instance.to_dict()
# create an instance of Solution from a dict
solution_from_dict = Solution.from_dict(solution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


