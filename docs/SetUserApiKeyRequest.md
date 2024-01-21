# SetUserApiKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name which will be assigned to the new api key. | 

## Example

```python
from arguflow.models.set_user_api_key_request import SetUserApiKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetUserApiKeyRequest from a JSON string
set_user_api_key_request_instance = SetUserApiKeyRequest.from_json(json)
# print the JSON string representation of the object
print SetUserApiKeyRequest.to_json()

# convert the object into a dict
set_user_api_key_request_dict = set_user_api_key_request_instance.to_dict()
# create an instance of SetUserApiKeyRequest from a dict
set_user_api_key_request_form_dict = set_user_api_key_request.from_dict(set_user_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


