# ChunkCollectionAndFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_id** | **str** |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**file_id** | **str** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from arguflow.models.chunk_collection_and_file import ChunkCollectionAndFile

# TODO update the JSON string below
json = "{}"
# create an instance of ChunkCollectionAndFile from a JSON string
chunk_collection_and_file_instance = ChunkCollectionAndFile.from_json(json)
# print the JSON string representation of the object
print ChunkCollectionAndFile.to_json()

# convert the object into a dict
chunk_collection_and_file_dict = chunk_collection_and_file_instance.to_dict()
# create an instance of ChunkCollectionAndFile from a dict
chunk_collection_and_file_form_dict = chunk_collection_and_file.from_dict(chunk_collection_and_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


