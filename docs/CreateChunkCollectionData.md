# CreateChunkCollectionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description to assign to the chunk_collection. Convenience field for you to avoid having to remember what the collection is for. | 
**name** | **str** | Name to assign to the chunk_collection. Does not need to be unique. | 

## Example

```python
from trieve_python_client.models.create_chunk_collection_data import CreateChunkCollectionData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChunkCollectionData from a JSON string
create_chunk_collection_data_instance = CreateChunkCollectionData.from_json(json)
# print the JSON string representation of the object
print CreateChunkCollectionData.to_json()

# convert the object into a dict
create_chunk_collection_data_dict = create_chunk_collection_data_instance.to_dict()
# create an instance of CreateChunkCollectionData from a dict
create_chunk_collection_data_form_dict = create_chunk_collection_data.from_dict(create_chunk_collection_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


