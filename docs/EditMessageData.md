# EditMessageData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_sort_order** | **int** | The sort order of the message to edit. | 
**model** | **str** | The model to use for the assistant generative inferences. This can be any model from the model list. If no model is provided, the gryphe/mythomax-l2-13b will be used.~ | [optional] 
**new_message_content** | **str** | The new content of the message to replace the old content with. | 
**topic_id** | **str** | The id of the topic to edit the message at the given sort order for. | 

## Example

```python
from trieve_python_client.models.edit_message_data import EditMessageData

# TODO update the JSON string below
json = "{}"
# create an instance of EditMessageData from a JSON string
edit_message_data_instance = EditMessageData.from_json(json)
# print the JSON string representation of the object
print EditMessageData.to_json()

# convert the object into a dict
edit_message_data_dict = edit_message_data_instance.to_dict()
# create an instance of EditMessageData from a dict
edit_message_data_form_dict = edit_message_data.from_dict(edit_message_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


