# AddChunkToCollectionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_id** | **str** | Id of the chunk to make a member of the collection. Think of this as \&quot;bookmark\&quot;ing a chunk. | 

## Example

```python
from trieve_python_client.models.add_chunk_to_collection_data import AddChunkToCollectionData

# TODO update the JSON string below
json = "{}"
# create an instance of AddChunkToCollectionData from a JSON string
add_chunk_to_collection_data_instance = AddChunkToCollectionData.from_json(json)
# print the JSON string representation of the object
print AddChunkToCollectionData.to_json()

# convert the object into a dict
add_chunk_to_collection_data_dict = add_chunk_to_collection_data_instance.to_dict()
# create an instance of AddChunkToCollectionData from a dict
add_chunk_to_collection_data_form_dict = add_chunk_to_collection_data.from_dict(add_chunk_to_collection_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


