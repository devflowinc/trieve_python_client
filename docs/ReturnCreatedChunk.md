# ReturnCreatedChunk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_metadata** | [**ChunkMetadata**](ChunkMetadata.md) |  | 
**duplicate** | **bool** |  | 

## Example

```python
from arguflow.models.return_created_chunk import ReturnCreatedChunk

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnCreatedChunk from a JSON string
return_created_chunk_instance = ReturnCreatedChunk.from_json(json)
# print the JSON string representation of the object
print ReturnCreatedChunk.to_json()

# convert the object into a dict
return_created_chunk_dict = return_created_chunk_instance.to_dict()
# create an instance of ReturnCreatedChunk from a dict
return_created_chunk_form_dict = return_created_chunk.from_dict(return_created_chunk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


