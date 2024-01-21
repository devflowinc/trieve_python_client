# BookmarkCollectionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_uuid** | **str** |  | 
**slim_collections** | [**List[SlimCollection]**](SlimCollection.md) |  | 

## Example

```python
from arguflow.models.bookmark_collection_result import BookmarkCollectionResult

# TODO update the JSON string below
json = "{}"
# create an instance of BookmarkCollectionResult from a JSON string
bookmark_collection_result_instance = BookmarkCollectionResult.from_json(json)
# print the JSON string representation of the object
print BookmarkCollectionResult.to_json()

# convert the object into a dict
bookmark_collection_result_dict = bookmark_collection_result_instance.to_dict()
# create an instance of BookmarkCollectionResult from a dict
bookmark_collection_result_form_dict = bookmark_collection_result.from_dict(bookmark_collection_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


