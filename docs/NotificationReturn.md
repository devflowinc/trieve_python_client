# NotificationReturn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_count** | **int** |  | 
**notifications** | [**List[Notification]**](Notification.md) |  | 
**total_pages** | **int** |  | 

## Example

```python
from arguflow.models.notification_return import NotificationReturn

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationReturn from a JSON string
notification_return_instance = NotificationReturn.from_json(json)
# print the JSON string representation of the object
print NotificationReturn.to_json()

# convert the object into a dict
notification_return_dict = notification_return_instance.to_dict()
# create an instance of NotificationReturn from a dict
notification_return_form_dict = notification_return.from_dict(notification_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


