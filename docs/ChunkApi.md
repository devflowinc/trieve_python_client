# arguflow.ChunkApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_chunk**](ChunkApi.md#create_chunk) | **POST** /api/chunk | create_chunk
[**create_suggested_queries_handler**](ChunkApi.md#create_suggested_queries_handler) | **POST** /api/chunk/gen_suggestions | get_suggested_queries
[**delete_chunk**](ChunkApi.md#delete_chunk) | **DELETE** /api/chunk/{chunk_id} | delete_chunk
[**delete_chunk_by_tracking_id**](ChunkApi.md#delete_chunk_by_tracking_id) | **DELETE** /api/chunk/tracking_id/{tracking_id} | delete_chunk_by_tracking_id
[**generate_off_chunks**](ChunkApi.md#generate_off_chunks) | **POST** /api/chunk/generate | generate_off_chunks
[**get_chunk_by_id**](ChunkApi.md#get_chunk_by_id) | **GET** /api/chunk/{chunk_id} | get_chunk
[**get_chunk_by_tracking_id**](ChunkApi.md#get_chunk_by_tracking_id) | **GET** /api/chunk/tracking_id/{tracking_id} | get_chunk_by_tracking_id
[**get_recommended_chunks**](ChunkApi.md#get_recommended_chunks) | **POST** /api/chunk/recommend | get_recommended_chunks
[**search_chunk**](ChunkApi.md#search_chunk) | **POST** /api/chunk/search | search
[**update_chunk**](ChunkApi.md#update_chunk) | **PUT** /api/chunk/update | update_chunk
[**update_chunk_by_tracking_id**](ChunkApi.md#update_chunk_by_tracking_id) | **PUT** /api/chunk/tracking_id/update | update_chunk_by_tracking_id


# **create_chunk**
> ReturnCreatedChunk create_chunk(create_chunk_data)

create_chunk

create_chunk  Create a new chunk. If the chunk has the same tracking_id as an existing chunk, the request will fail. Once a chunk is created, it can be searched for using the search endpoint.

### Example


```python
import arguflow
from arguflow.models.create_chunk_data import CreateChunkData
from arguflow.models.return_created_chunk import ReturnCreatedChunk
from arguflow.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = arguflow.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with arguflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = arguflow.ChunkApi(api_client)
    create_chunk_data = arguflow.CreateChunkData() # CreateChunkData | JSON request payload to create a new chunk (chunk)

    try:
        # create_chunk
        api_response = api_instance.create_chunk(create_chunk_data)
        print("The response of ChunkApi->create_chunk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkApi->create_chunk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_chunk_data** | [**CreateChunkData**](CreateChunkData.md)| JSON request payload to create a new chunk (chunk) | 

### Return type

[**ReturnCreatedChunk**](ReturnCreatedChunk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON response payload containing the created chunk |  -  |
**400** | Service error relating to to creating a chunk, likely due to conflicting tracking_id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_suggested_queries_handler**
> SuggestedQueriesResponse create_suggested_queries_handler(suggested_queries_request)

get_suggested_queries

get_suggested_queries  This endpoint will generate 3 suggested queries based off the query provided in the request body and return them as a JSON object.

### Example


```python
import arguflow
from arguflow.models.suggested_queries_request import SuggestedQueriesRequest
from arguflow.models.suggested_queries_response import SuggestedQueriesResponse
from arguflow.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = arguflow.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with arguflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = arguflow.ChunkApi(api_client)
    suggested_queries_request = arguflow.SuggestedQueriesRequest() # SuggestedQueriesRequest | JSON request payload to get alternative suggested queries

    try:
        # get_suggested_queries
        api_response = api_instance.create_suggested_queries_handler(suggested_queries_request)
        print("The response of ChunkApi->create_suggested_queries_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkApi->create_suggested_queries_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suggested_queries_request** | [**SuggestedQueriesRequest**](SuggestedQueriesRequest.md)| JSON request payload to get alternative suggested queries | 

### Return type

[**SuggestedQueriesResponse**](SuggestedQueriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object containing a list of alternative suggested queries |  -  |
**400** | Service error relating to to updating chunk, likely due to conflicting tracking_id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_chunk**
> delete_chunk(chunk_id)

delete_chunk

delete_chunk  Delete a chunk by its id. If deleting a root chunk which has a collision, the most recently created collision will become a new root chunk.

### Example


```python
import arguflow
from arguflow.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = arguflow.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with arguflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = arguflow.ChunkApi(api_client)
    chunk_id = 'chunk_id_example' # str | id of the chunk you want to delete

    try:
        # delete_chunk
        api_instance.delete_chunk(chunk_id)
    except Exception as e:
        print("Exception when calling ChunkApi->delete_chunk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chunk_id** | **str**| id of the chunk you want to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Confirmation that the chunk with the id specified was deleted |  -  |
**400** | Service error relating to finding a chunk by tracking_id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_chunk_by_tracking_id**
> delete_chunk_by_tracking_id(tracking_id)

delete_chunk_by_tracking_id

delete_chunk_by_tracking_id  Delete a chunk by tracking_id. This is useful for when you are coordinating with an external system and want to use the tracking_id to identify the chunk. If deleting a root chunk which has a collision, the most recently created collision will become a new root chunk.

### Example


```python
import arguflow
from arguflow.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = arguflow.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with arguflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = arguflow.ChunkApi(api_client)
    tracking_id = 'tracking_id_example' # str | tracking_id of the chunk you want to delete

    try:
        # delete_chunk_by_tracking_id
        api_instance.delete_chunk_by_tracking_id(tracking_id)
    except Exception as e:
        print("Exception when calling ChunkApi->delete_chunk_by_tracking_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracking_id** | **str**| tracking_id of the chunk you want to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Confirmation that the chunk with the tracking_id specified was deleted |  -  |
**400** | Service error relating to finding a chunk by tracking_id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_off_chunks**
> generate_off_chunks(generate_chunks_request)

generate_off_chunks

generate_off_chunks  This endpoint exists as an alternative to the topic+message concept where our API handles chat memory. With this endpoint, the user is responsible for providing the context window and the prompt. See more in the \"search before generate\" page at docs.trieve.ai.

### Example


```python
import arguflow
from arguflow.models.generate_chunks_request import GenerateChunksRequest
from arguflow.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = arguflow.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with arguflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = arguflow.ChunkApi(api_client)
    generate_chunks_request = arguflow.GenerateChunksRequest() # GenerateChunksRequest | JSON request payload to perform RAG on some chunks (chunks)

    try:
        # generate_off_chunks
        api_instance.generate_off_chunks(generate_chunks_request)
    except Exception as e:
        print("Exception when calling ChunkApi->generate_off_chunks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_chunks_request** | [**GenerateChunksRequest**](GenerateChunksRequest.md)| JSON request payload to perform RAG on some chunks (chunks) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This will be a HTTP stream of a string, check the chat or search UI for an example how to process this |  -  |
**400** | Service error relating to to updating chunk, likely due to conflicting tracking_id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chunk_by_id**
> ChunkMetadata get_chunk_by_id(chunk_id)

get_chunk

get_chunk  Get a singular chunk by id.

### Example


```python
import arguflow
from arguflow.models.chunk_metadata import ChunkMetadata
from arguflow.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = arguflow.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with arguflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = arguflow.ChunkApi(api_client)
    chunk_id = 'chunk_id_example' # str | Id of the chunk you want to fetch.

    try:
        # get_chunk
        api_response = api_instance.get_chunk_by_id(chunk_id)
        print("The response of ChunkApi->get_chunk_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkApi->get_chunk_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chunk_id** | **str**| Id of the chunk you want to fetch. | 

### Return type

[**ChunkMetadata**](ChunkMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | chunk with the id that you were searching for |  -  |
**400** | Service error relating to fidning a chunk by tracking_id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chunk_by_tracking_id**
> ChunkMetadata get_chunk_by_tracking_id(tracking_id)

get_chunk_by_tracking_id

get_chunk_by_tracking_id  Get a singular chunk by tracking_id. This is useful for when you are coordinating with an external system and want to use your own id as the primary reference for a chunk.

### Example


```python
import arguflow
from arguflow.models.chunk_metadata import ChunkMetadata
from arguflow.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = arguflow.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with arguflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = arguflow.ChunkApi(api_client)
    tracking_id = 'tracking_id_example' # str | tracking_id of the chunk you want to fetch

    try:
        # get_chunk_by_tracking_id
        api_response = api_instance.get_chunk_by_tracking_id(tracking_id)
        print("The response of ChunkApi->get_chunk_by_tracking_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkApi->get_chunk_by_tracking_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracking_id** | **str**| tracking_id of the chunk you want to fetch | 

### Return type

[**ChunkMetadata**](ChunkMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | chunk with the tracking_id that you were searching for |  -  |
**400** | Service error relating to fidning a chunk by tracking_id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommended_chunks**
> List[ChunkMetadataWithFileData] get_recommended_chunks(recommend_chunks_request)

get_recommended_chunks

get_recommended_chunks  Get recommendations of chunks similar to the chunks in the request. Think about this as a feature similar to the \"add to playlist\" recommendation feature on Spotify. This request pairs especially well with our collections endpoint.

### Example


```python
import arguflow
from arguflow.models.chunk_metadata_with_file_data import ChunkMetadataWithFileData
from arguflow.models.recommend_chunks_request import RecommendChunksRequest
from arguflow.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = arguflow.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with arguflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = arguflow.ChunkApi(api_client)
    recommend_chunks_request = arguflow.RecommendChunksRequest() # RecommendChunksRequest | JSON request payload to get recommendations of chunks similar to the chunks in the request

    try:
        # get_recommended_chunks
        api_response = api_instance.get_recommended_chunks(recommend_chunks_request)
        print("The response of ChunkApi->get_recommended_chunks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkApi->get_recommended_chunks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recommend_chunks_request** | [**RecommendChunksRequest**](RecommendChunksRequest.md)| JSON request payload to get recommendations of chunks similar to the chunks in the request | 

### Return type

[**List[ChunkMetadataWithFileData]**](ChunkMetadataWithFileData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON response payload containing chunks with scores which are similar to those in the request body |  -  |
**400** | Service error relating to to getting similar chunks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_chunk**
> SearchChunkQueryResponseBody search_chunk(search_chunk_data)

search

search  This route provides the primary search functionality for the API. It can be used to search for chunks by semantic similarity, full-text similarity, or a combination of both. Results' `chunk_html` values will be modified with `<b>` tags for sub-sentence highlighting.

### Example


```python
import arguflow
from arguflow.models.search_chunk_data import SearchChunkData
from arguflow.models.search_chunk_query_response_body import SearchChunkQueryResponseBody
from arguflow.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = arguflow.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with arguflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = arguflow.ChunkApi(api_client)
    search_chunk_data = arguflow.SearchChunkData() # SearchChunkData | JSON request payload to semantically search for chunks (chunks)

    try:
        # search
        api_response = api_instance.search_chunk(search_chunk_data)
        print("The response of ChunkApi->search_chunk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkApi->search_chunk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_chunk_data** | [**SearchChunkData**](SearchChunkData.md)| JSON request payload to semantically search for chunks (chunks) | 

### Return type

[**SearchChunkQueryResponseBody**](SearchChunkQueryResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | chunks which are similar to the embedding vector of the search query |  -  |
**400** | Service error relating to searching |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_chunk**
> update_chunk(update_chunk_data)

update_chunk

update_chunk  Update a chunk. If you try to change the tracking_id of the chunk to have the same tracking_id as an existing chunk, the request will fail.

### Example


```python
import arguflow
from arguflow.models.update_chunk_data import UpdateChunkData
from arguflow.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = arguflow.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with arguflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = arguflow.ChunkApi(api_client)
    update_chunk_data = arguflow.UpdateChunkData() # UpdateChunkData | JSON request payload to update a chunk (chunk)

    try:
        # update_chunk
        api_instance.update_chunk(update_chunk_data)
    except Exception as e:
        print("Exception when calling ChunkApi->update_chunk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_chunk_data** | [**UpdateChunkData**](UpdateChunkData.md)| JSON request payload to update a chunk (chunk) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content Ok response indicating the chunk was updated as requested |  -  |
**400** | Service error relating to to updating chunk, likely due to conflicting tracking_id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_chunk_by_tracking_id**
> update_chunk_by_tracking_id(update_chunk_by_tracking_id_data)

update_chunk_by_tracking_id

update_chunk_by_tracking_id  Update a chunk by tracking_id. This is useful for when you are coordinating with an external system and want to use the tracking_id to identify the chunk.

### Example


```python
import arguflow
from arguflow.models.update_chunk_by_tracking_id_data import UpdateChunkByTrackingIdData
from arguflow.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = arguflow.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with arguflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = arguflow.ChunkApi(api_client)
    update_chunk_by_tracking_id_data = arguflow.UpdateChunkByTrackingIdData() # UpdateChunkByTrackingIdData | JSON request payload to update a chunk by tracking_id (chunks)

    try:
        # update_chunk_by_tracking_id
        api_instance.update_chunk_by_tracking_id(update_chunk_by_tracking_id_data)
    except Exception as e:
        print("Exception when calling ChunkApi->update_chunk_by_tracking_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_chunk_by_tracking_id_data** | [**UpdateChunkByTrackingIdData**](UpdateChunkByTrackingIdData.md)| JSON request payload to update a chunk by tracking_id (chunks) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Confirmation that the chunk has been updated as per your request |  -  |
**400** | Service error relating to to updating chunk |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

