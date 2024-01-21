# CreateTopicData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_user_message** | **str** | The first message which will belong to the topic. The topic name is generated based on this message similar to how it works in the OpenAI chat UX. | 
**normal_chat** | **bool** | Whether or not RAG should be used on messages in this topic. | [optional] 

## Example

```python
from arguflow.models.create_topic_data import CreateTopicData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTopicData from a JSON string
create_topic_data_instance = CreateTopicData.from_json(json)
# print the JSON string representation of the object
print CreateTopicData.to_json()

# convert the object into a dict
create_topic_data_dict = create_topic_data_instance.to_dict()
# create an instance of CreateTopicData from a dict
create_topic_data_form_dict = create_topic_data.from_dict(create_topic_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


