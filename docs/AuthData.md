# AuthData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from trieve_python_client.models.auth_data import AuthData

# TODO update the JSON string below
json = "{}"
# create an instance of AuthData from a JSON string
auth_data_instance = AuthData.from_json(json)
# print the JSON string representation of the object
print AuthData.to_json()

# convert the object into a dict
auth_data_dict = auth_data_instance.to_dict()
# create an instance of AuthData from a dict
auth_data_form_dict = auth_data.from_dict(auth_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


