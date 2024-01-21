# FileUploadCompletedNotificationWithName


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
from arguflow.models.file_upload_completed_notification_with_name import FileUploadCompletedNotificationWithName

# TODO update the JSON string below
json = "{}"
# create an instance of FileUploadCompletedNotificationWithName from a JSON string
file_upload_completed_notification_with_name_instance = FileUploadCompletedNotificationWithName.from_json(json)
# print the JSON string representation of the object
print FileUploadCompletedNotificationWithName.to_json()

# convert the object into a dict
file_upload_completed_notification_with_name_dict = file_upload_completed_notification_with_name_instance.to_dict()
# create an instance of FileUploadCompletedNotificationWithName from a dict
file_upload_completed_notification_with_name_form_dict = file_upload_completed_notification_with_name.from_dict(file_upload_completed_notification_with_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


