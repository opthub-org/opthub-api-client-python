# GetSolution404Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from opthub_api_client.models.get_solution404_response import GetSolution404Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSolution404Response from a JSON string
get_solution404_response_instance = GetSolution404Response.from_json(json)
# print the JSON string representation of the object
print(GetSolution404Response.to_json())

# convert the object into a dict
get_solution404_response_dict = get_solution404_response_instance.to_dict()
# create an instance of GetSolution404Response from a dict
get_solution404_response_from_dict = GetSolution404Response.from_dict(get_solution404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


