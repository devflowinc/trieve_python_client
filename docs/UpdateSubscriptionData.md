# UpdateSubscriptionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** |  | 
**subscription_id** | **str** |  | 

## Example

```python
from arguflow.models.update_subscription_data import UpdateSubscriptionData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubscriptionData from a JSON string
update_subscription_data_instance = UpdateSubscriptionData.from_json(json)
# print the JSON string representation of the object
print UpdateSubscriptionData.to_json()

# convert the object into a dict
update_subscription_data_dict = update_subscription_data_instance.to_dict()
# create an instance of UpdateSubscriptionData from a dict
update_subscription_data_form_dict = update_subscription_data.from_dict(update_subscription_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


