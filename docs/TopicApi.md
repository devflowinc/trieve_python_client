# trieve_python_client.TopicApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_topic**](TopicApi.md#create_topic) | **POST** /api/topic | create_topic
[**delete_topic**](TopicApi.md#delete_topic) | **DELETE** /api/topic | delete_topic
[**get_all_topics**](TopicApi.md#get_all_topics) | **GET** /api/topic | get_all_topics
[**update_topic**](TopicApi.md#update_topic) | **PUT** /api/topic | update_topic


# **create_topic**
> Topic create_topic(create_topic_data)

create_topic

create_topic  Create a new chat topic. Topics are attached to a user and act as a coordinator for memory of gen-AI chat sessions. We are considering refactoring this resource of the API soon.

### Example


```python
import trieve_python_client
from trieve_python_client.models.create_topic_data import CreateTopicData
from trieve_python_client.models.topic import Topic
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
    api_instance = trieve_python_client.TopicApi(api_client)
    create_topic_data = trieve_python_client.CreateTopicData() # CreateTopicData | JSON request payload to create chat topic

    try:
        # create_topic
        api_response = api_instance.create_topic(create_topic_data)
        print("The response of TopicApi->create_topic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TopicApi->create_topic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_topic_data** | [**CreateTopicData**](CreateTopicData.md)| JSON request payload to create chat topic | 

### Return type

[**Topic**](Topic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The JSON response payload containing the created topic |  -  |
**400** | Topic name empty or a service error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_topic**
> delete_topic(delete_topic_data)

delete_topic

delete_topic  Delete an existing chat topic. When a topic is deleted, all associated chat messages are also deleted.

### Example


```python
import trieve_python_client
from trieve_python_client.models.delete_topic_data import DeleteTopicData
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
    api_instance = trieve_python_client.TopicApi(api_client)
    delete_topic_data = trieve_python_client.DeleteTopicData() # DeleteTopicData | JSON request payload to delete a chat topic

    try:
        # delete_topic
        api_instance.delete_topic(delete_topic_data)
    except Exception as e:
        print("Exception when calling TopicApi->delete_topic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_topic_data** | [**DeleteTopicData**](DeleteTopicData.md)| JSON request payload to delete a chat topic | 

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
**204** | Confirmation that the topic was deleted |  -  |
**400** | Service error relating to topic deletion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_topics**
> List[Topic] get_all_topics()

get_all_topics

get_all_topics  Get all topics belonging to a the auth'ed user. Soon, we plan to allow specification of the user for this route and include pagination.

### Example


```python
import trieve_python_client
from trieve_python_client.models.topic import Topic
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
    api_instance = trieve_python_client.TopicApi(api_client)

    try:
        # get_all_topics
        api_response = api_instance.get_all_topics()
        print("The response of TopicApi->get_all_topics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TopicApi->get_all_topics: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Topic]**](Topic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All topics belonging to a given user |  -  |
**400** | Service error relating to topic get |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_topic**
> update_topic(update_topic_data)

update_topic

update_topic  Update an existing chat topic. Currently, only the name of the topic can be updated.

### Example


```python
import trieve_python_client
from trieve_python_client.models.update_topic_data import UpdateTopicData
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
    api_instance = trieve_python_client.TopicApi(api_client)
    update_topic_data = trieve_python_client.UpdateTopicData() # UpdateTopicData | JSON request payload to update a chat topic

    try:
        # update_topic
        api_instance.update_topic(update_topic_data)
    except Exception as e:
        print("Exception when calling TopicApi->update_topic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_topic_data** | [**UpdateTopicData**](UpdateTopicData.md)| JSON request payload to update a chat topic | 

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
**204** | Confirmation that the topic was updated |  -  |
**400** | Service error relating to topic update |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

