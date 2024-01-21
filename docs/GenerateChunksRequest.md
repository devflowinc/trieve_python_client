# GenerateChunksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_ids** | **List[str]** | The ids of the chunks to be retrieved and injected into the context window for RAG. | 
**model** | **str** | The model to use for the chat. This can be any model from the model list. If no model is provided, the gryphe/mythomax-l2-13b will be used. | [optional] 
**prev_messages** | [**List[ChatMessageProxy]**](ChatMessageProxy.md) | The previous messages to be placed into the chat history. The last message in this array will be the prompt for the model to inference on. | 

## Example

```python
from arguflow.models.generate_chunks_request import GenerateChunksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateChunksRequest from a JSON string
generate_chunks_request_instance = GenerateChunksRequest.from_json(json)
# print the JSON string representation of the object
print GenerateChunksRequest.to_json()

# convert the object into a dict
generate_chunks_request_dict = generate_chunks_request_instance.to_dict()
# create an instance of GenerateChunksRequest from a dict
generate_chunks_request_form_dict = generate_chunks_request.from_dict(generate_chunks_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


