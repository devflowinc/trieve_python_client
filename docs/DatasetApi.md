# arguflow.DatasetApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dataset**](DatasetApi.md#create_dataset) | **POST** /api/dataset | create_dataset
[**delete_dataset**](DatasetApi.md#delete_dataset) | **DELETE** /api/dataset | delete_dataset
[**get_client_dataset_config**](DatasetApi.md#get_client_dataset_config) | **GET** /api/dataset/envs | get_client_dataset_config
[**get_dataset**](DatasetApi.md#get_dataset) | **GET** /api/dataset/{dataset_id} | get_dataset
[**get_datasets_from_organization**](DatasetApi.md#get_datasets_from_organization) | **GET** /api/dataset/organization/{organization_id} | get_organization_datasets
[**update_dataset**](DatasetApi.md#update_dataset) | **PUT** /api/dataset | update_dataset


# **create_dataset**
> Dataset create_dataset(create_dataset_request)

create_dataset

create_dataset  Create a new dataset. The auth'ed user must be an owner of the organization to create a dataset.

### Example


```python
import arguflow
from arguflow.models.create_dataset_request import CreateDatasetRequest
from arguflow.models.dataset import Dataset
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
    api_instance = arguflow.DatasetApi(api_client)
    create_dataset_request = arguflow.CreateDatasetRequest() # CreateDatasetRequest | JSON request payload to create a new dataset

    try:
        # create_dataset
        api_response = api_instance.create_dataset(create_dataset_request)
        print("The response of DatasetApi->create_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->create_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_dataset_request** | [**CreateDatasetRequest**](CreateDatasetRequest.md)| JSON request payload to create a new dataset | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset created successfully |  -  |
**400** | Service error relating to creating the dataset |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset**
> delete_dataset(delete_dataset_request)

delete_dataset

delete_dataset  Delete a dataset. The auth'ed user must be an owner of the organization to delete a dataset.

### Example


```python
import arguflow
from arguflow.models.delete_dataset_request import DeleteDatasetRequest
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
    api_instance = arguflow.DatasetApi(api_client)
    delete_dataset_request = arguflow.DeleteDatasetRequest() # DeleteDatasetRequest | JSON request payload to delete a dataset

    try:
        # delete_dataset
        api_instance.delete_dataset(delete_dataset_request)
    except Exception as e:
        print("Exception when calling DatasetApi->delete_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_dataset_request** | [**DeleteDatasetRequest**](DeleteDatasetRequest.md)| JSON request payload to delete a dataset | 

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
**204** | Dataset deleted successfully |  -  |
**400** | Service error relating to deleting the dataset |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_dataset_config**
> ClientDatasetConfiguration get_client_dataset_config()

get_client_dataset_config

get_client_dataset_config  Get the client configuration for a dataset. Will use the TR-D

### Example


```python
import arguflow
from arguflow.models.client_dataset_configuration import ClientDatasetConfiguration
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
    api_instance = arguflow.DatasetApi(api_client)

    try:
        # get_client_dataset_config
        api_response = api_instance.get_client_dataset_config()
        print("The response of DatasetApi->get_client_dataset_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->get_client_dataset_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClientDatasetConfiguration**](ClientDatasetConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset environment variables |  -  |
**400** | Service error relating to retrieving the dataset. Typically this only happens when your auth credentials are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset**
> Dataset get_dataset(dataset_id)

get_dataset

get_dataset  Get a dataset by id. The auth'ed user must be an admin or owner of the organization to get a dataset.

### Example


```python
import arguflow
from arguflow.models.dataset import Dataset
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
    api_instance = arguflow.DatasetApi(api_client)
    dataset_id = 'dataset_id_example' # str | The id of the dataset you want to retrieve.

    try:
        # get_dataset
        api_response = api_instance.get_dataset(dataset_id)
        print("The response of DatasetApi->get_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->get_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The id of the dataset you want to retrieve. | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset retrieved successfully |  -  |
**400** | Service error relating to retrieving the dataset |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasets_from_organization**
> List[DatasetAndUsage] get_datasets_from_organization(organization_id)

get_organization_datasets

get_organization_datasets  Get all datasets for an organization. The auth'ed user must be an admin or owner of the organization to get its datasets.

### Example


```python
import arguflow
from arguflow.models.dataset_and_usage import DatasetAndUsage
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
    api_instance = arguflow.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | id of the organization you want to retrieve datasets for

    try:
        # get_organization_datasets
        api_response = api_instance.get_datasets_from_organization(organization_id)
        print("The response of DatasetApi->get_datasets_from_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->get_datasets_from_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| id of the organization you want to retrieve datasets for | 

### Return type

[**List[DatasetAndUsage]**](DatasetAndUsage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Datasets retrieved successfully |  -  |
**400** | Service error relating to retrieving the dataset |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset**
> Dataset update_dataset(update_dataset_request)

update_dataset

update_dataset  Update a dataset. The auth'ed user must be an owner of the organization to update a dataset.

### Example


```python
import arguflow
from arguflow.models.dataset import Dataset
from arguflow.models.update_dataset_request import UpdateDatasetRequest
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
    api_instance = arguflow.DatasetApi(api_client)
    update_dataset_request = arguflow.UpdateDatasetRequest() # UpdateDatasetRequest | JSON request payload to update a dataset

    try:
        # update_dataset
        api_response = api_instance.update_dataset(update_dataset_request)
        print("The response of DatasetApi->update_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->update_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_dataset_request** | [**UpdateDatasetRequest**](UpdateDatasetRequest.md)| JSON request payload to update a dataset | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset updated successfully |  -  |
**400** | Service error relating to updating the dataset |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

