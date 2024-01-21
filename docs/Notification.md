# Notification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_name** | **str** |  | [optional] 
**collection_uuid** | **str** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**updated_at** | **datetime** |  | 
**user_read** | **bool** |  | 
**user_uuid** | **str** |  | 

## Example

```python
from arguflow.models.notification import Notification

# TODO update the JSON string below
json = "{}"
# create an instance of Notification from a JSON string
notification_instance = Notification.from_json(json)
# print the JSON string representation of the object
print Notification.to_json()

# convert the object into a dict
notification_dict = notification_instance.to_dict()
# create an instance of Notification from a dict
notification_form_dict = notification.from_dict(notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


