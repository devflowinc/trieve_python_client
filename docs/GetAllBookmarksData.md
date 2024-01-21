# GetAllBookmarksData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** |  | 
**page** | **int** |  | [optional] 

## Example

```python
from arguflow.models.get_all_bookmarks_data import GetAllBookmarksData

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllBookmarksData from a JSON string
get_all_bookmarks_data_instance = GetAllBookmarksData.from_json(json)
# print the JSON string representation of the object
print GetAllBookmarksData.to_json()

# convert the object into a dict
get_all_bookmarks_data_dict = get_all_bookmarks_data_instance.to_dict()
# create an instance of GetAllBookmarksData from a dict
get_all_bookmarks_data_form_dict = get_all_bookmarks_data.from_dict(get_all_bookmarks_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


