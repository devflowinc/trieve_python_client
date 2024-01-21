# CollectionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collections** | [**List[ChunkCollectionAndFile]**](ChunkCollectionAndFile.md) |  | 
**total_pages** | **int** |  | 

## Example

```python
from arguflow.models.collection_data import CollectionData

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionData from a JSON string
collection_data_instance = CollectionData.from_json(json)
# print the JSON string representation of the object
print CollectionData.to_json()

# convert the object into a dict
collection_data_dict = collection_data_instance.to_dict()
# create an instance of CollectionData from a dict
collection_data_form_dict = collection_data.from_dict(collection_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


