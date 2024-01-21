# arguflow.FileApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_file_handler**](FileApi.md#delete_file_handler) | **DELETE** /api/file/{file_id} | delete_file
[**get_file_handler**](FileApi.md#get_file_handler) | **GET** /api/file/{file_id} | get_file
[**get_image_file**](FileApi.md#get_image_file) | **GET** /api/image/{file_name} | get_image_file
[**upload_file_handler**](FileApi.md#upload_file_handler) | **POST** /api/file | upload_file


# **delete_file_handler**
> delete_file_handler(file_id)

delete_file

delete_file  Delete a file from S3 attached to the server based on its id. This will disassociate chunks from the file, but will not delete the chunks. We plan to add support for deleting chunks in a release soon. Auth'ed user must be an admin or owner of the dataset's organization to upload a file.

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
    api_instance = arguflow.FileApi(api_client)
    file_id = 'file_id_example' # str | The id of the file to delete

    try:
        # delete_file
        api_instance.delete_file_handler(file_id)
    except Exception as e:
        print("Exception when calling FileApi->delete_file_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The id of the file to delete | 

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
**204** | Confirmation that the file has been deleted |  -  |
**400** | Service error relating to finding or deleting the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_handler**
> FileDTO get_file_handler(file_id)

get_file

get_file  Download a file from S3 attached to the server based on its id. We plan to add support for getting signed S3 URLs to download from S3 directly in a release soon.

### Example


```python
import arguflow
from arguflow.models.file_dto import FileDTO
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
    api_instance = arguflow.FileApi(api_client)
    file_id = 'file_id_example' # str | The id of the file to fetch

    try:
        # get_file
        api_response = api_instance.get_file_handler(file_id)
        print("The response of FileApi->get_file_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->get_file_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The id of the file to fetch | 

### Return type

[**FileDTO**](FileDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The file corresponding to the file_id requested |  -  |
**400** | Service error relating to finding the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_file**
> get_image_file(file_name)

get_image_file

get_image_file  We strongly recommend not using this endpoint. It is disabled on the managed version and only meant for niche on-prem use cases where an image directory is mounted. Get in touch with us thru information on docs.trieve.ai for more information.

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
    api_instance = arguflow.FileApi(api_client)
    file_name = 'file_name_example' # str | The name of the image file to return

    try:
        # get_image_file
        api_instance.get_image_file(file_name)
    except Exception as e:
        print("Exception when calling FileApi->get_image_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| The name of the image file to return | 

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
**200** | The raw image file corresponding to the file_name requested such that it can be a src for an img tag |  -  |
**400** | Service error relating to finding the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file_handler**
> UploadFileResult upload_file_handler(upload_file_data)

upload_file

upload_file  Upload a file to S3 attached to the server. The file will be converted to HTML with tika and chunked algorithmically, images will be OCR'ed with tesseract. The resulting chunks will be indexed and searchable. Optionally, you can only upload the file and manually create chunks associated to the file after. See docs.trieve.ai and/or contact us for more details and tips. Auth'ed user must be an admin or owner of the dataset's organization to upload a file.

### Example


```python
import arguflow
from arguflow.models.upload_file_data import UploadFileData
from arguflow.models.upload_file_result import UploadFileResult
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
    api_instance = arguflow.FileApi(api_client)
    upload_file_data = arguflow.UploadFileData() # UploadFileData | JSON request payload to upload a file

    try:
        # upload_file
        api_response = api_instance.upload_file_handler(upload_file_data)
        print("The response of FileApi->upload_file_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->upload_file_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_file_data** | [**UploadFileData**](UploadFileData.md)| JSON request payload to upload a file | 

### Return type

[**UploadFileResult**](UploadFileResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirmation that the file is uploading |  -  |
**400** | Service error relating to uploading the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

