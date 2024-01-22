# trieve_python_client.UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_api_key**](UserApi.md#delete_user_api_key) | **DELETE** /api/user/delete_api_key | delete_user_api_key
[**get_user_files_handler**](UserApi.md#get_user_files_handler) | **GET** /api/user/files/{user_id} | get_user_files
[**get_user_with_chunks_by_id**](UserApi.md#get_user_with_chunks_by_id) | **GET** /api/user/{user_id}/{page} | get_user_chunks
[**set_user_api_key**](UserApi.md#set_user_api_key) | **POST** /api/user/set_api_key | set_user_api_key
[**update_user**](UserApi.md#update_user) | **PUT** /api/user | update_user


# **delete_user_api_key**
> List[ApiKeyDTO] delete_user_api_key(delete_user_api_key_request)

delete_user_api_key

delete_user_api_key  Delete an api key for the auth'ed user.

### Example


```python
import trieve_python_client
from trieve_python_client.models.api_key_dto import ApiKeyDTO
from trieve_python_client.models.delete_user_api_key_request import DeleteUserApiKeyRequest
from trieve_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with trieve_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_python_client.UserApi(api_client)
    delete_user_api_key_request = trieve_python_client.DeleteUserApiKeyRequest() # DeleteUserApiKeyRequest | JSON request payload to delete a user api key

    try:
        # delete_user_api_key
        api_response = api_instance.delete_user_api_key(delete_user_api_key_request)
        print("The response of UserApi->delete_user_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->delete_user_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_user_api_key_request** | [**DeleteUserApiKeyRequest**](DeleteUserApiKeyRequest.md)| JSON request payload to delete a user api key | 

### Return type

[**List[ApiKeyDTO]**](ApiKeyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON body representing the api_key for the user |  -  |
**400** | Service error relating to creating api_key for the user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_files_handler**
> List[File] get_user_files_handler(user_id)

get_user_files

get_user_files  Get all files which belong to a given user specified by the user_id parameter.

### Example


```python
import trieve_python_client
from trieve_python_client.models.file import File
from trieve_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with trieve_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_python_client.UserApi(api_client)
    user_id = 'user_id_example' # str | The id of the user to fetch files for.

    try:
        # get_user_files
        api_response = api_instance.get_user_files_handler(user_id)
        print("The response of UserApi->get_user_files_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_files_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user to fetch files for. | 

### Return type

[**List[File]**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON body representing the files uploaded by the given user |  -  |
**400** | Service error relating to getting the files uploaded by the given user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_with_chunks_by_id**
> UserDTOWithChunks get_user_with_chunks_by_id(user_id, page)

get_user_chunks

get_user_chunks  Get the chunks which were made by a given user.

### Example


```python
import trieve_python_client
from trieve_python_client.models.user_dto_with_chunks import UserDTOWithChunks
from trieve_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with trieve_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_python_client.UserApi(api_client)
    user_id = 'user_id_example' # str | The id of the user to fetch.
    page = 56 # int | The page of chunks to fetch. Each page is 10 chunks. Support for custom page size is coming soon.

    try:
        # get_user_chunks
        api_response = api_instance.get_user_with_chunks_by_id(user_id, page)
        print("The response of UserApi->get_user_with_chunks_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_with_chunks_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user to fetch. | 
 **page** | **int**| The page of chunks to fetch. Each page is 10 chunks. Support for custom page size is coming soon. | 

### Return type

[**UserDTOWithChunks**](UserDTOWithChunks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON body representing the chunks made by a given user with their chunks |  -  |
**400** | Service error relating to getting the chunks for the given user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_api_key**
> SetUserApiKeyResponse set_user_api_key(set_user_api_key_request)

set_user_api_key

set_user_api_key  Create a new api key for the auth'ed user. Successful response will contain the newly created api key.

### Example


```python
import trieve_python_client
from trieve_python_client.models.set_user_api_key_request import SetUserApiKeyRequest
from trieve_python_client.models.set_user_api_key_response import SetUserApiKeyResponse
from trieve_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with trieve_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_python_client.UserApi(api_client)
    set_user_api_key_request = trieve_python_client.SetUserApiKeyRequest() # SetUserApiKeyRequest | 

    try:
        # set_user_api_key
        api_response = api_instance.set_user_api_key(set_user_api_key_request)
        print("The response of UserApi->set_user_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->set_user_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_user_api_key_request** | [**SetUserApiKeyRequest**](SetUserApiKeyRequest.md)|  | 

### Return type

[**SetUserApiKeyResponse**](SetUserApiKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON body representing the api_key for the user |  -  |
**400** | Service error relating to creating api_key for the user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> SlimUser update_user(update_user_data)

update_user

update_user  Update a user's information. If the user_id is not provided, the auth'ed user will be updated. If the user_id is provided, the auth'ed user must be an admin (1) or owner (2) of the organization.

### Example


```python
import trieve_python_client
from trieve_python_client.models.slim_user import SlimUser
from trieve_python_client.models.update_user_data import UpdateUserData
from trieve_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with trieve_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_python_client.UserApi(api_client)
    update_user_data = trieve_python_client.UpdateUserData() # UpdateUserData | JSON request payload to update user information for the auth'ed user

    try:
        # update_user
        api_response = api_instance.update_user(update_user_data)
        print("The response of UserApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_user_data** | [**UpdateUserData**](UpdateUserData.md)| JSON request payload to update user information for the auth&#39;ed user | 

### Return type

[**SlimUser**](SlimUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON body representing the updated user information |  -  |
**400** | Service error relating to updating the user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

