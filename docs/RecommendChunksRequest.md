# RecommendChunksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**positive_chunk_ids** | **List[str]** | The ids of the chunks to be used as positive examples for the recommendation. The chunks in this array will be used to find similar chunks. | 

## Example

```python
from arguflow.models.recommend_chunks_request import RecommendChunksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendChunksRequest from a JSON string
recommend_chunks_request_instance = RecommendChunksRequest.from_json(json)
# print the JSON string representation of the object
print RecommendChunksRequest.to_json()

# convert the object into a dict
recommend_chunks_request_dict = recommend_chunks_request_instance.to_dict()
# create an instance of RecommendChunksRequest from a dict
recommend_chunks_request_form_dict = recommend_chunks_request.from_dict(recommend_chunks_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


