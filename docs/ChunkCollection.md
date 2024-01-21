# ChunkCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_id** | **str** |  | 
**created_at** | **datetime** |  | 
**dataset_id** | **str** |  | 
**description** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from arguflow.models.chunk_collection import ChunkCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ChunkCollection from a JSON string
chunk_collection_instance = ChunkCollection.from_json(json)
# print the JSON string representation of the object
print ChunkCollection.to_json()

# convert the object into a dict
chunk_collection_dict = chunk_collection_instance.to_dict()
# create an instance of ChunkCollection from a dict
chunk_collection_form_dict = chunk_collection.from_dict(chunk_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


