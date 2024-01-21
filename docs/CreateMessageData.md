# CreateMessageData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | The model to use for the assistant&#39;s messages. This can be any model from the model list. If no model is provided, the gryphe/mythomax-l2-13b will be used. | [optional] 
**new_message_content** | **str** | The content of the user message to attach to the topic and then generate an assistant message in response to. | 
**topic_id** | **str** | The ID of the topic to attach the message to. | 

## Example

```python
from arguflow.models.create_message_data import CreateMessageData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMessageData from a JSON string
create_message_data_instance = CreateMessageData.from_json(json)
# print the JSON string representation of the object
print CreateMessageData.to_json()

# convert the object into a dict
create_message_data_dict = create_message_data_instance.to_dict()
# create an instance of CreateMessageData from a dict
create_message_data_form_dict = create_message_data.from_dict(create_message_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


