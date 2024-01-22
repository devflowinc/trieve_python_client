# CreateChunkData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_html** | **str** | HTML content of the chunk. This can also be plaintext. The innerText of the HTML will be used to create the embedding vector. The point of using HTML is for convienience, as some users have applications where users submit HTML content. | [optional] 
**chunk_vector** | **List[float]** | Chunk_vector is a vector of floats which can be used instead of generating a new embedding. This is useful for when you are using a pre-embedded dataset. If this is not provided, the innerText of the chunk_html will be used to create the embedding. | [optional] 
**collection_id** | **str** | Collection_id is the id of the collection that the chunk should be placed into. This is useful for when you want to create a chunk and add it to a collection in one request. | [optional] 
**file_uuid** | **str** | File_uuid is the uuid of the file that the chunk is associated with. This is used to associate chunks with files. This is useful for when you want to delete a file and all of its associated chunks. | [optional] 
**link** | **str** | Link to the chunk. This can also be any string. Frequently, this is a link to the source of the chunk. The link value will not affect the embedding creation. | [optional] 
**metadata** | **object** | Metadata is a JSON object which can be used to filter chunks. This is useful for when you want to filter chunks by arbitrary metadata. Unlike with tag filtering, there is a performance hit for filtering on metadata. | [optional] 
**tag_set** | **str** | Tag set is a comma separated list of tags. This can be used to filter chunks by tag. Unlike with metadata filtering, HNSW indices will exist for each tag such that there is not a performance hit for filtering on them. | [optional] 
**time_stamp** | **str** | Time_stamp should be an ISO 8601 combined date and time without timezone. It is used for time window filtering and recency-biasing search results. | [optional] 
**tracking_id** | **str** | Tracking_id is a string which can be used to identify a chunk. This is useful for when you are coordinating with an external system and want to use the tracking_id to identify the chunk. | [optional] 
**weight** | **float** | Weight is a float which can be used to bias search results. This is useful for when you want to bias search results for a chunk. The magnitude only matters relative to other chunks in the chunk&#39;s dataset dataset. | [optional] 

## Example

```python
from trieve_python_client.models.create_chunk_data import CreateChunkData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChunkData from a JSON string
create_chunk_data_instance = CreateChunkData.from_json(json)
# print the JSON string representation of the object
print CreateChunkData.to_json()

# convert the object into a dict
create_chunk_data_dict = create_chunk_data_instance.to_dict()
# create an instance of CreateChunkData from a dict
create_chunk_data_form_dict = create_chunk_data.from_dict(create_chunk_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


