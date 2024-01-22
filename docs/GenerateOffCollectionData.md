# GenerateOffCollectionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** |  | 
**page** | **int** |  | [optional] 
**query** | **str** |  | [optional] 

## Example

```python
from trieve_python_client.models.generate_off_collection_data import GenerateOffCollectionData

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateOffCollectionData from a JSON string
generate_off_collection_data_instance = GenerateOffCollectionData.from_json(json)
# print the JSON string representation of the object
print GenerateOffCollectionData.to_json()

# convert the object into a dict
generate_off_collection_data_dict = generate_off_collection_data_instance.to_dict()
# create an instance of GenerateOffCollectionData from a dict
generate_off_collection_data_form_dict = generate_off_collection_data.from_dict(generate_off_collection_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


