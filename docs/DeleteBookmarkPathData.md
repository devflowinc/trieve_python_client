# DeleteBookmarkPathData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookmark_id** | **str** |  | 
**collection_id** | **str** |  | 

## Example

```python
from trieve_python_client.models.delete_bookmark_path_data import DeleteBookmarkPathData

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteBookmarkPathData from a JSON string
delete_bookmark_path_data_instance = DeleteBookmarkPathData.from_json(json)
# print the JSON string representation of the object
print DeleteBookmarkPathData.to_json()

# convert the object into a dict
delete_bookmark_path_data_dict = delete_bookmark_path_data_instance.to_dict()
# create an instance of DeleteBookmarkPathData from a dict
delete_bookmark_path_data_form_dict = delete_bookmark_path_data.from_dict(delete_bookmark_path_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


