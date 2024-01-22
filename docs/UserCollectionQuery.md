# UserCollectionQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**user_id** | **str** |  | 

## Example

```python
from trieve_python_client.models.user_collection_query import UserCollectionQuery

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionQuery from a JSON string
user_collection_query_instance = UserCollectionQuery.from_json(json)
# print the JSON string representation of the object
print UserCollectionQuery.to_json()

# convert the object into a dict
user_collection_query_dict = user_collection_query_instance.to_dict()
# create an instance of UserCollectionQuery from a dict
user_collection_query_form_dict = user_collection_query.from_dict(user_collection_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


