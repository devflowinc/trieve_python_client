# UpdateChunkData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_html** | **str** | HTML content of the chunk you want to update. This can also be plaintext. The innerText of the HTML will be used to create the embedding vector. The point of using HTML is for convienience, as some users have applications where users submit HTML content. If no chunk_html is provided, the existing chunk_html will be used. | [optional] 
**chunk_uuid** | **str** | Id of the chunk you want to update. | 
**link** | **str** | Link of the chunk you want to update. This can also be any string. Frequently, this is a link to the source of the chunk. The link value will not affect the embedding creation. If no link is provided, the existing link will be used. | [optional] 
**metadata** | **object** | The metadata is a JSON object which can be used to filter chunks. This is useful for when you want to filter chunks by arbitrary metadata. Unlike with tag filtering, there is a performance hit for filtering on metadata. If no metadata is provided, the existing metadata will be used. | [optional] 
**time_stamp** | **str** | Time_stamp should be an ISO 8601 combined date and time without timezone. It is used for time window filtering and recency-biasing search results. If no time_stamp is provided, the existing time_stamp will be used. | [optional] 
**tracking_id** | **str** | Tracking_id is a string which can be used to identify a chunk. This is useful for when you are coordinating with an external system and want to use the tracking_id to identify the chunk. If no tracking_id is provided, the existing tracking_id will be used. | [optional] 
**weight** | **float** | Weight is a float which can be used to bias search results. This is useful for when you want to bias search results for a chunk. The magnitude only matters relative to other chunks in the chunk&#39;s dataset dataset. If no weight is provided, the existing weight will be used. | [optional] 

## Example

```python
from arguflow.models.update_chunk_data import UpdateChunkData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateChunkData from a JSON string
update_chunk_data_instance = UpdateChunkData.from_json(json)
# print the JSON string representation of the object
print UpdateChunkData.to_json()

# convert the object into a dict
update_chunk_data_dict = update_chunk_data_instance.to_dict()
# create an instance of UpdateChunkData from a dict
update_chunk_data_form_dict = update_chunk_data.from_dict(update_chunk_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


