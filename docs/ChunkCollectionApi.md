# arguflow.ChunkCollectionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_bookmark**](ChunkCollectionApi.md#add_bookmark) | **POST** /api/chunk_collection/{collection_id} | add_bookmark
[**create_chunk_collection**](ChunkCollectionApi.md#create_chunk_collection) | **POST** /api/chunk_collection | create_chunk_collection
[**delete_bookmark**](ChunkCollectionApi.md#delete_bookmark) | **DELETE** /api/bookmark/{collection_id}/{bookmark_id} | delete_bookmark
[**delete_chunk_collection**](ChunkCollectionApi.md#delete_chunk_collection) | **DELETE** /api/chunk_collection/{collection_id} | delete_chunk_collection
[**get_all_bookmarks**](ChunkCollectionApi.md#get_all_bookmarks) | **GET** /api/chunk_collection/{collection_id}/{page} | get_all_bookmarks
[**get_collections_chunk_is_in**](ChunkCollectionApi.md#get_collections_chunk_is_in) | **POST** /api/chunk_collection/bookmark | 
[**get_logged_in_user_chunk_collections**](ChunkCollectionApi.md#get_logged_in_user_chunk_collections) | **GET** /api/chunk_collection/{page} | get_current_user_collections
[**get_specific_user_chunk_collections**](ChunkCollectionApi.md#get_specific_user_chunk_collections) | **GET** /api/user/collections/{user_id}/{page} | get_user_collections
[**search_collections**](ChunkCollectionApi.md#search_collections) | **POST** /api/chunk_collection/search | collection_search
[**update_chunk_collection**](ChunkCollectionApi.md#update_chunk_collection) | **PUT** /api/chunk_collection | update_chunk_collection


# **add_bookmark**
> add_bookmark(collection_id, add_chunk_to_collection_data)

add_bookmark

add_bookmark  Route to add a bookmark. Think of a bookmark as a chunk which is a member of a collection.

### Example


```python
import arguflow
from arguflow.models.add_chunk_to_collection_data import AddChunkToCollectionData
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
    api_instance = arguflow.ChunkCollectionApi(api_client)
    collection_id = 'collection_id_example' # str | Id of the collection to add the chunk to as a bookmark
    add_chunk_to_collection_data = arguflow.AddChunkToCollectionData() # AddChunkToCollectionData | JSON request payload to add a chunk to a collection (bookmark it)

    try:
        # add_bookmark
        api_instance.add_bookmark(collection_id, add_chunk_to_collection_data)
    except Exception as e:
        print("Exception when calling ChunkCollectionApi->add_bookmark: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Id of the collection to add the chunk to as a bookmark | 
 **add_chunk_to_collection_data** | [**AddChunkToCollectionData**](AddChunkToCollectionData.md)| JSON request payload to add a chunk to a collection (bookmark it) | 

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
**204** | Confirmation that the chunk was added to the collection (bookmark&#39;ed). |  -  |
**400** | Service error relating to getting the collections that the chunk is in. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_chunk_collection**
> ChunkCollection create_chunk_collection(create_chunk_collection_data)

create_chunk_collection

create_chunk_collection  Create a new chunk_collection. Think of this as analogous to a bookmark folder.

### Example


```python
import arguflow
from arguflow.models.chunk_collection import ChunkCollection
from arguflow.models.create_chunk_collection_data import CreateChunkCollectionData
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
    api_instance = arguflow.ChunkCollectionApi(api_client)
    create_chunk_collection_data = arguflow.CreateChunkCollectionData() # CreateChunkCollectionData | JSON request payload to cretea a chunkCollection

    try:
        # create_chunk_collection
        api_response = api_instance.create_chunk_collection(create_chunk_collection_data)
        print("The response of ChunkCollectionApi->create_chunk_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkCollectionApi->create_chunk_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_chunk_collection_data** | [**CreateChunkCollectionData**](CreateChunkCollectionData.md)| JSON request payload to cretea a chunkCollection | 

### Return type

[**ChunkCollection**](ChunkCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the created chunkCollection |  -  |
**400** | Service error relating to creating the chunkCollection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bookmark**
> delete_bookmark(collection_id, bookmark_id)

delete_bookmark

delete_bookmark  Route to delete a bookmark. Think of a bookmark as a chunk which is a member of a collection.

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
    api_instance = arguflow.ChunkCollectionApi(api_client)
    collection_id = 'collection_id_example' # str | Id of the collection to remove the bookmark'ed chunk from
    bookmark_id = 'bookmark_id_example' # str | Id of the bookmark to remove

    try:
        # delete_bookmark
        api_instance.delete_bookmark(collection_id, bookmark_id)
    except Exception as e:
        print("Exception when calling ChunkCollectionApi->delete_bookmark: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Id of the collection to remove the bookmark&#39;ed chunk from | 
 **bookmark_id** | **str**| Id of the bookmark to remove | 

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
**204** | Confirmation that the chunk was removed to the collection |  -  |
**400** | Service error relating to removing the chunk from the collection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_chunk_collection**
> delete_chunk_collection(collection_id)

delete_chunk_collection

delete_chunk_collection  This will delete a chunk_collection. This will not delete the chunks that are in the collection. We will soon support deleting a chunk_collection along with its member chunks.

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
    api_instance = arguflow.ChunkCollectionApi(api_client)
    collection_id = 'collection_id_example' # str | Id of the chunk_collection to delete

    try:
        # delete_chunk_collection
        api_instance.delete_chunk_collection(collection_id)
    except Exception as e:
        print("Exception when calling ChunkCollectionApi->delete_chunk_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Id of the chunk_collection to delete | 

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
**204** | Confirmation that the chunkCollection was deleted |  -  |
**400** | Service error relating to deleting the chunkCollection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_bookmarks**
> BookmarkData get_all_bookmarks(collection_id, page)

get_all_bookmarks

get_all_bookmarks  Route to get all bookmarks for a collection. Think of a bookmark as a chunk which is a member of a collection. The response is paginated, with each page containing 10 chunks (bookmarks). Support for custom page size is coming soon.

### Example


```python
import arguflow
from arguflow.models.bookmark_data import BookmarkData
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
    api_instance = arguflow.ChunkCollectionApi(api_client)
    collection_id = 'collection_id_example' # str | The id of the collection to get the chunks from
    page = 56 # int | The page of chunks to get from the collection

    try:
        # get_all_bookmarks
        api_response = api_instance.get_all_bookmarks(collection_id, page)
        print("The response of ChunkCollectionApi->get_all_bookmarks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkCollectionApi->get_all_bookmarks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The id of the collection to get the chunks from | 
 **page** | **int**| The page of chunks to get from the collection | 

### Return type

[**BookmarkData**](BookmarkData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bookmark&#39;ed chunks present within the specified collection |  -  |
**400** | Service error relating to getting the collections that the chunk is in |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collections_chunk_is_in**
> List[BookmarkCollectionResult] get_collections_chunk_is_in(get_collections_for_chunks_data)



### Example


```python
import arguflow
from arguflow.models.bookmark_collection_result import BookmarkCollectionResult
from arguflow.models.get_collections_for_chunks_data import GetCollectionsForChunksData
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
    api_instance = arguflow.ChunkCollectionApi(api_client)
    get_collections_for_chunks_data = arguflow.GetCollectionsForChunksData() # GetCollectionsForChunksData | JSON request payload to get the collections that a chunk is in

    try:
        api_response = api_instance.get_collections_chunk_is_in(get_collections_for_chunks_data)
        print("The response of ChunkCollectionApi->get_collections_chunk_is_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkCollectionApi->get_collections_chunk_is_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_collections_for_chunks_data** | [**GetCollectionsForChunksData**](GetCollectionsForChunksData.md)| JSON request payload to get the collections that a chunk is in | 

### Return type

[**List[BookmarkCollectionResult]**](BookmarkCollectionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON body representing the collections that the chunk is in |  -  |
**400** | Service error relating to getting the collections that the chunk is in |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logged_in_user_chunk_collections**
> CollectionData get_logged_in_user_chunk_collections(page)

get_current_user_collections

get_current_user_collections  Fetch the collections which belong to the currently logged in user. We are soon going to refactor collections to relate to only datasets instead of datasets and users.

### Example


```python
import arguflow
from arguflow.models.collection_data import CollectionData
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
    api_instance = arguflow.ChunkCollectionApi(api_client)
    page = 56 # int | The page of collections to fetch

    try:
        # get_current_user_collections
        api_response = api_instance.get_logged_in_user_chunk_collections(page)
        print("The response of ChunkCollectionApi->get_logged_in_user_chunk_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkCollectionApi->get_logged_in_user_chunk_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of collections to fetch | 

### Return type

[**CollectionData**](CollectionData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The page of collections for the auth&#39;ed user |  -  |
**400** | Service error relating to getting the collections for the auth&#39;ed user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_specific_user_chunk_collections**
> CollectionData get_specific_user_chunk_collections(user_id, page)

get_user_collections

get_user_collections  Fetch the collections which belong to a user specified by their id. We are soon going to refactor collections to relate to only datasets instead of datasets and users.

### Example


```python
import arguflow
from arguflow.models.collection_data import CollectionData
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
    api_instance = arguflow.ChunkCollectionApi(api_client)
    user_id = 'user_id_example' # str | The id of the user to fetch collections for.
    page = 56 # int | The page of collections to fetch. Each page contains 10 collections. Support for custom page size is coming soon.

    try:
        # get_user_collections
        api_response = api_instance.get_specific_user_chunk_collections(user_id, page)
        print("The response of ChunkCollectionApi->get_specific_user_chunk_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkCollectionApi->get_specific_user_chunk_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user to fetch collections for. | 
 **page** | **int**| The page of collections to fetch. Each page contains 10 collections. Support for custom page size is coming soon. | 

### Return type

[**CollectionData**](CollectionData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON body representing the collections created by the given user |  -  |
**400** | Service error relating to getting the collections created by the given user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_collections**
> SearchCollectionsResult search_collections(search_collections_data)

collection_search

collection_search  This route allows you to search only within a collection. This is useful for when you only want search results to contain chunks which are members of a specific group. Think about this like searching within a playlist or bookmark folder.

### Example


```python
import arguflow
from arguflow.models.search_collections_data import SearchCollectionsData
from arguflow.models.search_collections_result import SearchCollectionsResult
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
    api_instance = arguflow.ChunkCollectionApi(api_client)
    search_collections_data = arguflow.SearchCollectionsData() # SearchCollectionsData | JSON request payload to semantically search a collection

    try:
        # collection_search
        api_response = api_instance.search_collections(search_collections_data)
        print("The response of ChunkCollectionApi->search_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkCollectionApi->search_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_collections_data** | [**SearchCollectionsData**](SearchCollectionsData.md)| JSON request payload to semantically search a collection | 

### Return type

[**SearchCollectionsResult**](SearchCollectionsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collection chunks which are similar to the embedding vector of the search query |  -  |
**400** | Service error relating to getting the collections that the chunk is in |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_chunk_collection**
> update_chunk_collection(update_chunk_collection_data)

update_chunk_collection

update_chunk_collection  Update a chunk_collection. Think of this as analogous to a bookmark folder.

### Example


```python
import arguflow
from arguflow.models.update_chunk_collection_data import UpdateChunkCollectionData
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
    api_instance = arguflow.ChunkCollectionApi(api_client)
    update_chunk_collection_data = arguflow.UpdateChunkCollectionData() # UpdateChunkCollectionData | JSON request payload to update a chunkCollection

    try:
        # update_chunk_collection
        api_instance.update_chunk_collection(update_chunk_collection_data)
    except Exception as e:
        print("Exception when calling ChunkCollectionApi->update_chunk_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_chunk_collection_data** | [**UpdateChunkCollectionData**](UpdateChunkCollectionData.md)| JSON request payload to update a chunkCollection | 

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
**204** | Confirmation that the chunkCollection was updated |  -  |
**400** | Service error relating to updating the chunkCollection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

