# UpdateChunkCollectionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** | Id of the chunk_collection to update. | 
**description** | **str** | Description to assign to the chunk_collection. Convenience field for you to avoid having to remember what the collection is for. If not provided, the description will not be updated. | [optional] 
**name** | **str** | Name to assign to the chunk_collection. Does not need to be unique. If not provided, the name will not be updated. | [optional] 

## Example

```python
from trieve_python_client.models.update_chunk_collection_data import UpdateChunkCollectionData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateChunkCollectionData from a JSON string
update_chunk_collection_data_instance = UpdateChunkCollectionData.from_json(json)
# print the JSON string representation of the object
print UpdateChunkCollectionData.to_json()

# convert the object into a dict
update_chunk_collection_data_dict = update_chunk_collection_data_instance.to_dict()
# create an instance of UpdateChunkCollectionData from a dict
update_chunk_collection_data_form_dict = update_chunk_collection_data.from_dict(update_chunk_collection_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


