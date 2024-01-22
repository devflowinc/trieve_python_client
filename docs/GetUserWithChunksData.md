# GetUserWithChunksData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | The page of chunks to fetch. Each page is 10 chunks. Support for custom page size is coming soon. | 
**user_id** | **str** | The id of the user to fetch the chunks for. | 

## Example

```python
from trieve_python_client.models.get_user_with_chunks_data import GetUserWithChunksData

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserWithChunksData from a JSON string
get_user_with_chunks_data_instance = GetUserWithChunksData.from_json(json)
# print the JSON string representation of the object
print GetUserWithChunksData.to_json()

# convert the object into a dict
get_user_with_chunks_data_dict = get_user_with_chunks_data_instance.to_dict()
# create an instance of GetUserWithChunksData from a dict
get_user_with_chunks_data_form_dict = get_user_with_chunks_data.from_dict(get_user_with_chunks_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


