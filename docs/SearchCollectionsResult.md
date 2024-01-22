# SearchCollectionsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookmarks** | [**List[ScoreChunkDTO]**](ScoreChunkDTO.md) |  | 
**collection** | [**ChunkCollection**](ChunkCollection.md) |  | 
**total_pages** | **int** |  | 

## Example

```python
from trieve_python_client.models.search_collections_result import SearchCollectionsResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchCollectionsResult from a JSON string
search_collections_result_instance = SearchCollectionsResult.from_json(json)
# print the JSON string representation of the object
print SearchCollectionsResult.to_json()

# convert the object into a dict
search_collections_result_dict = search_collections_result_instance.to_dict()
# create an instance of SearchCollectionsResult from a dict
search_collections_result_form_dict = search_collections_result.from_dict(search_collections_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


