# SearchCollectionsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** | Collection_id specifies the collection to search within. Results will only consist of chunks which are bookmarks within the specified collection. | 
**date_bias** | **bool** | Set date_bias to true to bias search results towards more recent chunks. This will work best in hybrid search mode. | [optional] 
**filters** | **object** | Filters is a JSON object which can be used to filter chunks. The values on each key in the object will be used to check for an exact substring match on the metadata values for each existing chunk. This is useful for when you want to filter chunks by arbitrary metadata. Unlike with tag filtering, there is a performance hit for filtering on metadata. | [optional] 
**link** | **List[str]** | The link set is a comma separated list of links. This can be used to filter chunks by link. HNSW indices do not exist for links, so there is a performance hit for filtering on them. | [optional] 
**page** | **int** | The page of chunks to fetch. Each page is 10 chunks. Support for custom page size is coming soon. | [optional] 
**query** | **str** | The query is the search query. This can be any string. The query will be used to create an embedding vector and/or SPLADE vector which will be used to find the result set. | 
**search_type** | **str** | Search_type can be either \&quot;semantic\&quot;, \&quot;fulltext\&quot;, or \&quot;hybrid\&quot;. \&quot;hybrid\&quot; will pull in one page (10 chunks) of both semantic and full-text results then re-rank them using BAAI/bge-reranker-large. \&quot;semantic\&quot; will pull in one page (10 chunks) of the nearest cosine distant vectors. \&quot;fulltext\&quot; will pull in one page (10 chunks) of full-text results based on SPLADE. | 
**tag_set** | **List[str]** | The tag set is a comma separated list of tags. This can be used to filter chunks by tag. Unlike with metadata filtering, HNSW indices will exist for each tag such that there is not a performance hit for filtering on them. | [optional] 

## Example

```python
from trieve_python_client.models.search_collections_data import SearchCollectionsData

# TODO update the JSON string below
json = "{}"
# create an instance of SearchCollectionsData from a JSON string
search_collections_data_instance = SearchCollectionsData.from_json(json)
# print the JSON string representation of the object
print SearchCollectionsData.to_json()

# convert the object into a dict
search_collections_data_dict = search_collections_data_instance.to_dict()
# create an instance of SearchCollectionsData from a dict
search_collections_data_form_dict = search_collections_data.from_dict(search_collections_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


