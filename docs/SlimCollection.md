# SlimCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_id** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**of_current_user** | **bool** |  | 

## Example

```python
from arguflow.models.slim_collection import SlimCollection

# TODO update the JSON string below
json = "{}"
# create an instance of SlimCollection from a JSON string
slim_collection_instance = SlimCollection.from_json(json)
# print the JSON string representation of the object
print SlimCollection.to_json()

# convert the object into a dict
slim_collection_dict = slim_collection_instance.to_dict()
# create an instance of SlimCollection from a dict
slim_collection_form_dict = slim_collection.from_dict(slim_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


