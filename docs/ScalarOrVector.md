# ScalarOrVector

A double-precision floating-point scalar or vector.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vector** | **List[float]** | A double-precision floating-point vector. | [optional] 
**scalar** | **float** | A double-precision floating-point scalar value | [optional] 

## Example

```python
from opthub_api_client.models.scalar_or_vector import ScalarOrVector

# TODO update the JSON string below
json = "{}"
# create an instance of ScalarOrVector from a JSON string
scalar_or_vector_instance = ScalarOrVector.from_json(json)
# print the JSON string representation of the object
print(ScalarOrVector.to_json())

# convert the object into a dict
scalar_or_vector_dict = scalar_or_vector_instance.to_dict()
# create an instance of ScalarOrVector from a dict
scalar_or_vector_from_dict = ScalarOrVector.from_dict(scalar_or_vector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


