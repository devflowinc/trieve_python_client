# SearchChunkData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cross_encoder** | **bool** | Set cross_encoder to true to use the BAAI/bge-reranker-large model to re-rank search results. This will only apply if in hybrid search mode. If no weighs are specified, the re-ranker will be used by default. | [optional] 
**date_bias** | **bool** | Set date_bias to true to bias search results towards more recent chunks. This will work best in hybrid search mode. | [optional] 
**filters** | **object** | Filters is a JSON object which can be used to filter chunks. The values on each key in the object will be used to check for an exact substring match on the metadata values for each existing chunk. This is useful for when you want to filter chunks by arbitrary metadata. Unlike with tag filtering, there is a performance hit for filtering on metadata. | [optional] 
**link** | **List[str]** | Link set is a comma separated list of links. This can be used to filter chunks by link. HNSW indices do not exist for links, so there is a performance hit for filtering on them. | [optional] 
**page** | **int** | Page of chunks to fetch. Each page is 10 chunks. Support for custom page size is coming soon. | [optional] 
**query** | **str** | Query is the search query. This can be any string. The query will be used to create an embedding vector and/or SPLADE vector which will be used to find the result set. | 
**search_type** | **str** | Can be either \&quot;semantic\&quot;, \&quot;fulltext\&quot;, or \&quot;hybrid\&quot;. \&quot;hybrid\&quot; will pull in one page (10 chunks) of both semantic and full-text results then re-rank them using reciprocal rank fusion using the specified weights or BAAI/bge-reranker-large. \&quot;semantic\&quot; will pull in one page (10 chunks) of the nearest cosine distant vectors. \&quot;fulltext\&quot; will pull in one page (10 chunks) of full-text results based on SPLADE. | 
**tag_set** | **List[str]** | Tag_set is a comma separated list of tags. This can be used to filter chunks by tag. Unlike with metadata filtering, HNSW indices will exist for each tag such that there is not a performance hit for filtering on them. | [optional] 
**time_range** | [**List[SearchChunkDataTimeRangeInner]**](SearchChunkDataTimeRangeInner.md) | Time_range is a tuple of two ISO 8601 combined date and time without timezone. The first value is the start of the time range and the second value is the end of the time range. This can be used to filter chunks by time range. HNSW indices do not exist for time range, so there is a performance hit for filtering on them. | [optional] 
**weights** | [**List[SearchChunkDataWeightsInner]**](SearchChunkDataWeightsInner.md) | Weights are a tuple of two floats. The first value is the weight for the semantic search results and the second value is the weight for the full-text search results. This can be used to bias search results towards semantic or full-text results. This will only apply if in hybrid search mode and cross_encoder is set to false. | [optional] 

## Example

```python
from arguflow.models.search_chunk_data import SearchChunkData

# TODO update the JSON string below
json = "{}"
# create an instance of SearchChunkData from a JSON string
search_chunk_data_instance = SearchChunkData.from_json(json)
# print the JSON string representation of the object
print SearchChunkData.to_json()

# convert the object into a dict
search_chunk_data_dict = search_chunk_data_instance.to_dict()
# create an instance of SearchChunkData from a dict
search_chunk_data_form_dict = search_chunk_data.from_dict(search_chunk_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


