# FileDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base64url_content** | **str** |  | 
**created_at** | **datetime** |  | 
**file_name** | **str** |  | 
**id** | **str** |  | 
**link** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**size** | **int** |  | 
**updated_at** | **datetime** |  | 
**user_id** | **str** |  | 

## Example

```python
from trieve_python_client.models.file_dto import FileDTO

# TODO update the JSON string below
json = "{}"
# create an instance of FileDTO from a JSON string
file_dto_instance = FileDTO.from_json(json)
# print the JSON string representation of the object
print FileDTO.to_json()

# convert the object into a dict
file_dto_dict = file_dto_instance.to_dict()
# create an instance of FileDTO from a dict
file_dto_form_dict = file_dto.from_dict(file_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


