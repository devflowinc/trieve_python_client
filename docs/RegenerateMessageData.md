# RegenerateMessageData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | The model to use for the assistant generative inferences. This can be any model from the model list. If no model is provided, the gryphe/mythomax-l2-13b will be used.~ | [optional] 
**topic_id** | **str** | The id of the topic to regenerate the last message for. | 

## Example

```python
from trieve_python_client.models.regenerate_message_data import RegenerateMessageData

# TODO update the JSON string below
json = "{}"
# create an instance of RegenerateMessageData from a JSON string
regenerate_message_data_instance = RegenerateMessageData.from_json(json)
# print the JSON string representation of the object
print RegenerateMessageData.to_json()

# convert the object into a dict
regenerate_message_data_dict = regenerate_message_data_instance.to_dict()
# create an instance of RegenerateMessageData from a dict
regenerate_message_data_form_dict = regenerate_message_data.from_dict(regenerate_message_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


