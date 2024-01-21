# GetDirectPaymentLinkData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | 
**plan_id** | **str** |  | 

## Example

```python
from arguflow.models.get_direct_payment_link_data import GetDirectPaymentLinkData

# TODO update the JSON string below
json = "{}"
# create an instance of GetDirectPaymentLinkData from a JSON string
get_direct_payment_link_data_instance = GetDirectPaymentLinkData.from_json(json)
# print the JSON string representation of the object
print GetDirectPaymentLinkData.to_json()

# convert the object into a dict
get_direct_payment_link_data_dict = get_direct_payment_link_data_instance.to_dict()
# create an instance of GetDirectPaymentLinkData from a dict
get_direct_payment_link_data_form_dict = get_direct_payment_link_data.from_dict(get_direct_payment_link_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


