# UserDTOWithChunks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunks** | [**List[ChunkMetadataWithFileData]**](ChunkMetadataWithFileData.md) |  | 
**created_at** | **datetime** |  | 
**email** | **str** |  | [optional] 
**id** | **str** |  | 
**total_chunks_created** | **int** |  | 
**username** | **str** |  | [optional] 
**visible_email** | **bool** |  | 
**website** | **str** |  | [optional] 

## Example

```python
from trieve_python_client.models.user_dto_with_chunks import UserDTOWithChunks

# TODO update the JSON string below
json = "{}"
# create an instance of UserDTOWithChunks from a JSON string
user_dto_with_chunks_instance = UserDTOWithChunks.from_json(json)
# print the JSON string representation of the object
print UserDTOWithChunks.to_json()

# convert the object into a dict
user_dto_with_chunks_dict = user_dto_with_chunks_instance.to_dict()
# create an instance of UserDTOWithChunks from a dict
user_dto_with_chunks_form_dict = user_dto_with_chunks.from_dict(user_dto_with_chunks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


