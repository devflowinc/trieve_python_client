# BookmarkChunks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[ChunkMetadataWithFileData]**](ChunkMetadataWithFileData.md) |  | 

## Example

```python
from trieve_python_client.models.bookmark_chunks import BookmarkChunks

# TODO update the JSON string below
json = "{}"
# create an instance of BookmarkChunks from a JSON string
bookmark_chunks_instance = BookmarkChunks.from_json(json)
# print the JSON string representation of the object
print BookmarkChunks.to_json()

# convert the object into a dict
bookmark_chunks_dict = bookmark_chunks_instance.to_dict()
# create an instance of BookmarkChunks from a dict
bookmark_chunks_form_dict = bookmark_chunks.from_dict(bookmark_chunks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


