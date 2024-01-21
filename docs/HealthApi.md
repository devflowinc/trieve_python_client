# arguflow.HealthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check**](HealthApi.md#health_check) | **GET** /api/health | 


# **health_check**
> health_check()



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
    api_instance = arguflow.HealthApi(api_client)

    try:
        api_instance.health_check()
    except Exception as e:
        print("Exception when calling HealthApi->health_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Confirmation that the service is healthy and can make embedding vectors |  -  |
**400** | Service error relating to making an embedding or overall service health |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

